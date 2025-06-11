from fastapi import FastAPI
from api.routers import quote, tickers

app = FastAPI()

app.include_router(quote.router, prefix="/api")
app.include_router(tickers.router, prefix="/api")


@app.get("/")
def root():
    return {"status": "marketpulse backend is live"}
