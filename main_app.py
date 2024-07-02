import logging

from fastapi import FastAPI
import httpx

logger = logging.getLogger(__name__)
app = FastAPI()


@app.get("/forward")
async def forward():
    logger.info("forwarding request to nginx server")
    async with httpx.AsyncClient() as client:
        response = await client.get("http://nginx:8080/backend")
    return response.json()
