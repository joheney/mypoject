import pytest
from myproject.app import app
from fastapi.testclient import TestClient  # type: ignore

import pytest_asyncio # type: ignore
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine

from sqlalchemy.pool import StaticPool


# @pytest_asyncio.fixture
# async def session():
#     engine = create_async_engine(
#         "sqlite+aiosqlite:///:memory:",
#         connect_args={"check_same_thread": False},
#         poolclass=StaticPool,
#     )
#     async with engine.begin() as conn:
#         await conn.run_sync(table_registry.metadata.create_all)

#     async with AsyncSession(engine, expire_on_commit=False) as session:
#         yield session

#     async with engine.begin() as conn:
#         await conn.run_sync(table_registry.metadata.drop_all)
