import asyncio
from processing.consumer import consume_and_store

if __name__ == "__main__":
    asyncio.run(consume_and_store('marketpulse.trades'))

