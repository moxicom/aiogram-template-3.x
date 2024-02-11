from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine, AsyncAttrs
from sqlalchemy.orm import declarative_base
import logging

logger = logging.getLogger(__name__)

engine : AsyncEngine = create_async_engine("postgresql+asyncpg://postgres:postgres@localhost:5432/postgres")

Base = declarative_base()
