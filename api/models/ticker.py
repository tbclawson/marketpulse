from pydantic import BaseModel

class Ticker(BaseModel):
    symbol: str
    name: str
    exchange: str
    currency: str
    type: str
