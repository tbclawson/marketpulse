import asyncpg
import logging
import json
from datetime import datetime, timezone
from api.config import settings

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


class Storage:
    def __init__(self):
        self._pool = None

    async def connect(self):
        self._pool = await asyncpg.create_pool(
            host=settings.postgres_host,
            port=settings.postgres_port,
            database=settings.postgres_db,
            user=settings.postgres_user,
            password=settings.postgres_password,
            min_size=1,
            max_size=5
        )
        logger.info("DB connection pool created.")

    async def insert_trade(self, trade_data: dict):
        """
        Insert trade or analytics data into DB.
        trade_data should have keys: symbol, price, volume, ts, indicators
        """

        if not self._pool:
            raise RuntimeError("Storage not connected — call connect() before inserting.")
        
        ts_dt = datetime.fromtimestamp(trade_data['ts'] / 1000.0, tz=timezone.utc)


        async with self._pool.acquire() as conn:
            await conn.execute(
                """
                INSERT INTO trades (symbol, price, volume, ts, conditions, indicators)
                VALUES ($1, $2, $3, $4, $5, $6)
                """,
                trade_data['symbol'],
                trade_data['price'],
                trade_data['volume'],
                ts_dt,
                trade_data['conditions'],
                json.dumps(trade_data.get('indicators')) if trade_data.get('indicators') else None
            )
            logger.info(f"Stored trade for {trade_data['symbol']} at {trade_data['ts']}")

    async def close(self):
        if self._pool:
            await self._pool.close()
            logger.info("DB connection pool closed.")
# Placeholder Python module


