from sqlmodel import SQLModel, Field
from datetime import datetime
from typing import Optional


class Counter(SQLModel, table=True):
    """Counter model for storing counter values with history tracking."""

    __tablename__ = "counters"  # type: ignore[assignment]

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(max_length=100, default="default")
    value: int = Field(default=0)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class CounterUpdate(SQLModel, table=False):
    """Schema for updating counter values."""

    value: Optional[int] = Field(default=None)
    name: Optional[str] = Field(default=None, max_length=100)


class CounterCreate(SQLModel, table=False):
    """Schema for creating new counters."""

    name: str = Field(max_length=100, default="default")
    value: int = Field(default=0)


class CounterResponse(SQLModel, table=False):
    """Schema for counter API responses."""

    id: int
    name: str
    value: int
    created_at: str
    updated_at: str
