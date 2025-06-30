from typing import List
from urllib.parse import quote_plus

import motor.motor_asyncio
from beanie import Document
from fastapi_users.db import BaseOAuthAccount, BeanieBaseUser, BeanieUserDatabase
from pydantic import Field

from .settings import settings

DATABASE_URL = f"mongodb+srv://{settings.MONGO_USER}:{quote_plus(settings.MONGO_PASSWORD)}@{settings.MONGO_HOST}/?retryWrites=true&w=majority&appName={settings.MONGO_CLUSTER}"
client = motor.motor_asyncio.AsyncIOMotorClient(
    DATABASE_URL, uuidRepresentation="standard"
)  # type: ignore
db = client[settings.MONGO_DB]


class OAuthAccount(BaseOAuthAccount):
    pass


class User(BeanieBaseUser, Document):
    oauth_accounts: List[OAuthAccount] = Field(default_factory=list)


async def get_user_db():
    yield BeanieUserDatabase(User, OAuthAccount)
