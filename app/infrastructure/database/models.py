from datetime import datetime

from sqlalchemy import DateTime, Numeric, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class OrderModel(Base):

    __tablename__ = "orders"

    id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True
    )

    customer_id: Mapped[str] = mapped_column(
        String(50),
        nullable=False
    )

    total_amount: Mapped[float] = mapped_column(
        Numeric(10, 2),
        nullable=False
    )

    status: Mapped[str] = mapped_column(
        String(20),
        nullable=False
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False
    )