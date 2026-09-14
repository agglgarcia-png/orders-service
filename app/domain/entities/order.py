from dataclasses import dataclass
from datetime import UTC, datetime
from decimal import Decimal
from uuid import UUID

from app.domain.exceptions.order_exceptions import (
    CustomerRequiredError,
    InvalidOrderAmountError,
    InvalidOrderStatusTransitionError,
)
from app.domain.value_objects.order_status import OrderStatus


@dataclass
class Order:
    id: UUID
    customer_id: str
    total_amount: Decimal
    status: OrderStatus
    created_at: datetime
    updated_at: datetime

    def __post_init__(self) -> None:

        if not self.customer_id:
            raise CustomerRequiredError(
                "Customer ID is required"
            )

        if self.total_amount <= Decimal(0):
            raise InvalidOrderAmountError(
                "Order amount must be greater than zero"
            )

    def mark_as_processing(self) -> None:

        if self.status != OrderStatus.PENDING:
            raise InvalidOrderStatusTransitionError(
                "Only pending orders can be processed"
            )

        self.status = OrderStatus.PROCESSING
        self.updated_at = datetime.now(UTC)

    def mark_as_shipped(self) -> None:

        if self.status != OrderStatus.PROCESSING:
            raise InvalidOrderStatusTransitionError(
                "Only processing orders can be shipped"
            )

        self.status = OrderStatus.SHIPPED
        self.updated_at = datetime.now(UTC)

    def mark_as_delivered(self) -> None:

        if self.status != OrderStatus.SHIPPED:
            raise InvalidOrderStatusTransitionError(
                "Only shipped orders can be delivered"
            )

        self.status = OrderStatus.DELIVERED
        self.updated_at = datetime.now(UTC)

    def cancel(self) -> None:

        if self.status in (
            OrderStatus.DELIVERED,
            OrderStatus.CANCELLED,
        ):
            raise InvalidOrderStatusTransitionError(
                "Order cannot be cancelled"
            )

        self.status = OrderStatus.CANCELLED
        self.updated_at = datetime.now(UTC)