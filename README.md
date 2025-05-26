# Real-time Repository Event Webhook Feed

## Overview

This is a feed of a number of repository events webhook deliveries that gets updated in real time.

## Prerequisite

* Smee client (can be installed with `npm install --global smee-client`)

## Steps to test

* run `pip install -r requirements.txt`
* `smee --url https://smee.io/H4RV9oWjWigm2OP6 --path /webhook --port 8000`
* set environment variable WEBHOOK_SECRET to qaswcdefvrbtghnyydfscvpoijuh in the .env file
* run `fastapi dev main.py`
* the app is already installed in the repository for testing

## What I have done

### Backend

* Setup an async queue to recieve events
* The webhook deliveries are validated using their SHA256 signatures
* The real time feed is implemented using a Server Sent Event system using StreamingResponse from FastAPI

### Frontend

* Made with very basic DOM manipulation


## TODO

1. The async queue is limited by memory and can be used for only one repo. This needs to be replaced by something like Apache Kafka to resolve this limitation.
2. The provision for handling the exception of client disconnect is not implemented yet.
3. The frontend needs to be reworked. The present implementation is very basic.
4. With 1. done the app can be extended for use in other repositories.
