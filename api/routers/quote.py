from fastapi import APIRouter, HTTPException
from api.services.finnhub import get_stock_quote

router = APIRouter()

@router.get("/quote/{symbol}")
async def get_quote(symbol: str):
    try:
        data = await get_stock_quote(symbol.upper())
        return {"symbol": symbol.upper(), "data": data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
