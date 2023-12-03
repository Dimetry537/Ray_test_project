from src.db.base import get_async_session
from sqlalchemy.ext.asyncio import AsyncSession

class BaseRepository:
    def __init__(self, session: AsyncSession = None):
        self.session = session

    async def connect(self):
        if self.session is None:
            self.session = await get_async_session().__anext__()

    async def disconnect(self):
        if self.session:
            await self.session.close()

    async def __aenter__(self):
        await self.connect()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.disconnect()
