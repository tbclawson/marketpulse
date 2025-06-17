import asyncio
from data_ingestion.stream_listener import listen_to_trades
from processing.consumer import consume_and_store

async def main():
    symbols = ['AAPL', 'TSLA', 'MSFT']  # Your symbols to subscribe to

    # Run both the stream listener and consumer concurrently
    await asyncio.gather(
        listen_to_trades(symbols),
        consume_and_store('marketpulse.trades')
    )

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Pipeline shutdown requested by user.")
