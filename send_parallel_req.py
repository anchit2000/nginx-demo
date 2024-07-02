import httpx
import asyncio


async def send_request():
    async with httpx.AsyncClient() as client:
        response = await client.get("http://localhost:8000/forward")
        print(response.json())


async def main():
    tasks = [send_request() for _ in range(10)]
    await asyncio.gather(*tasks)


asyncio.run(main())
