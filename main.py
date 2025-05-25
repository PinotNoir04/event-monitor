import asyncio
import hashlib
import hmac
import json
import logging
import os

from dotenv import load_dotenv
from fastapi import FastAPI, Header, HTTPException, Request
from fastapi.responses import StreamingResponse
from fastapi.staticfiles import StaticFiles

load_dotenv()

WEBHOOK_SECRET = os.getenv("WEBHOOK_SECRET")

app = FastAPI()

queue = asyncio.Queue()


def verify_signature(body, signature):
    if not signature:
        logging.error("Signature Missing")
        return False
    if not WEBHOOK_SECRET:
        logging.error("Webhook Secret Missing")
        return False

    expected_signature = "sha256=" + hmac.new(WEBHOOK_SECRET.encode("utf-8"), body, hashlib.sha256).hexdigest()

    logging.info("Verified")
    return hmac.compare_digest(signature, expected_signature)


@app.post("/webhook")
async def webhook(req: Request, x_hub_signature_256: str = Header(None)):
    body = await req.body()

    if not verify_signature(body, x_hub_signature_256):
        raise HTTPException(status_code=403, detail="Wrong Signature")

    try:
        payload = json.loads(body.decode("utf-8"))
    except:
        raise Exception("Could not parse payload")

    await queue.put(payload)

    return {"status": "ok"}


async def events_generator():
    while True:
        data = await queue.get()
        yield f"data: {json.dumps(data)}\n\n"
        queue.task_done()


@app.get("/events")
async def events():
    return StreamingResponse(events_generator(), media_type="text/event-stream")
