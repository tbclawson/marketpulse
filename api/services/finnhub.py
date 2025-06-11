import httpx
from api.config import settings
from api.models.ticker import Ticker

FINNHUB_BASE_URL = "https://finnhub.io/api/v1"

async def get_stock_quote(symbol: str) -> dict:
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"{FINNHUB_BASE_URL}/quote",
            params={"symbol": symbol, "token": settings.finnhub_api_key}
        )
        response.raise_for_status()
        return response.json()


async def get_us_tickers() -> list[Ticker]:
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"{FINNHUB_BASE_URL}/stock/symbol",
            params={"exchange": "US", "token": settings.finnhub_api_key}
        )
        response.raise_for_status()
        raw_data = response.json()

        # Convert each item into a Ticker object
        tickers = [
            Ticker(
                symbol=item["symbol"],
                name=item["description"],
                exchange=item["mic"],
                currency=item["currency"],
                type=item["type"]
            )
            for item in raw_data
        ]
        return tickers