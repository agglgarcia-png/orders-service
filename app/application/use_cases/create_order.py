from datetime import UTC, datetime
from decimal import Decimal
from uuid import uuid4

from app.domain.entities.order import Order
from app.domain.repositories.order_repository import OrderRepository
from app.domain.value_objects.order_status import OrderStatus


class CreateOrderUseCase:

    def __init__(
        self,
        repository: OrderRepository
    ):
        self.repository = repository

    def execute(
        self,
        customer_id: str,
        total_amount: Decimal,
    ) -> Order:

        now = datetime.now(UTC)

        order = Order(
            id=uuid4(),
            customer_id=customer_id,
            total_amount=total_amount,
            status=OrderStatus.PENDING,
            created_at=now,
            updated_at=now,
        )

        self.repository.save(order)

        return order