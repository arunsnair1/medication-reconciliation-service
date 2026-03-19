import os
from motor.motor_asyncio import AsyncIOMotorClient
from app.core.config import settings

MONGO_URL = os.getenv("MONGO_URL")

client = AsyncIOMotorClient(MONGO_URL)

db = client[settings.DB_NAME]