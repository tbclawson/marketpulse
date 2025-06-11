import asyncio
from data_ingestion.stream_listener import listen_to_trades

if __name__ == "__main__":
    asyncio.run(listen_to_trades(["AAPL", "MSFT", "TSLA"]))
    
