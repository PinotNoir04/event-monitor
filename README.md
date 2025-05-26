# Real-time Repository Event Webhook Feed

## Overview

This is a feed of a number of repository events webhook deliveries that get updated in real time.

## Steps to setup
```
* Install the Github App
* View the events in the feed page
```

## What I have done

### Backend

* Setup an async queue to recieve events
* The webhook deliveries are validated using their SHA256 signatures
* The real time feed is implemented using a Server Sent Event system using StreamingResponse from FastAPI

### Frontend

* Made with very basic DOM manipulation
* The feed is not updating even though the SSE endpoint is working


## TODO

1. The async queue is limited by memory and can be used for only one repo. This needs to be replaced by something like Apache Kafka to resolve this limitation.
2. The provision for handling the exception of client disconnect is not implemented yet.
3. The frontend needs to be reworked. The present implementation is very basic.
