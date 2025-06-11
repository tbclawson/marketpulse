import asyncio
import websockets
import json
from api.config import settings

FINNHUB_WS_URL = f"wss://ws.finnhub.io?token={settings.finnhub_api_key}"

async def listen_to_trades(symbols: list[str]):
    async with websockets.connect(FINNHUB_WS_URL) as ws:
        # Subscribe to all symbols
        for symbol in symbols:
            await ws.send(json.dumps({"type": "subscribe", "symbol": symbol}))
            print(f"Subscribed to {symbol}")

        # Continuously receive data
        while True:
            try:
                msg = await ws.recv()
                print(msg)  # Eventually publish to Kafka
            except Exception as e:
                print("WebSocket error:", e)
                await asyncio.sleep(5)  # Reconnect delay
