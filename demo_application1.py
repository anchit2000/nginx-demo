import logging

from fastapi import FastAPI
import asyncio

logger = logging.getLogger(__name__)
app = FastAPI()


@app.get("/backend")
async def backend():
    logger.info("Request receieved on server number 1")
    await asyncio.sleep(2)  # Simulate processing delay
    return {"message": "Hello from backend 1!"}
