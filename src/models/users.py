from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import String, Boolean, Column

from fastapi_users.db import SQLAlchemyBaseUserTableUUID
from src.db.base import Base

class User(SQLAlchemyBaseUserTableUUID, Base):
    id = Column(UUID(as_uuid=True), unique=True, primary_key=True, index=True)
    email = Column(String(length=320), unique=True, index=True, nullable=False)
    hashed_password = Column(String(length=1024), nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)
    is_superuser = Column(Boolean, default=False, nullable=False)
    is_verified = Column(Boolean, default=False, nullable=False)

