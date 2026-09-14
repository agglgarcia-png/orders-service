from datetime import datetime
from decimal import Decimal
from uuid import UUID

from pydantic import BaseModel

from app.domain.value_objects.order_status import (
    OrderStatus,
)


class CreateOrderRequest(BaseModel):
    customer_id: str
    total_amount: Decimal


class UpdateOrderStatusRequest(
    BaseModel
):
    status: OrderStatus


class OrderResponse(BaseModel):

    id: UUID
    customer_id: str
    total_amount: Decimal
    status: str
    created_at: datetime
    updated_at: datetime