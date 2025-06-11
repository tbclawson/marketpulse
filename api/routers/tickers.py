from fastapi import APIRouter, HTTPException
from typing import List
from api.services.finnhub import get_us_tickers
from api.models.ticker import Ticker

router = APIRouter()

@router.get("/tickers", response_model=List[Ticker])
async def get_tickers():
    try:
        data = await get_us_tickers()
        return data
    except Exception as e:
        print(f"Error in /tickers: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
