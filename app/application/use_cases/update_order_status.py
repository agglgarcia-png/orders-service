from uuid import UUID

from app.domain.entities.order import Order
from app.domain.exceptions.order_exceptions import (
    OrderNotFoundError,
)
from app.domain.repositories.order_repository import (
    OrderRepository,
)
from app.domain.value_objects.order_status import (
    OrderStatus,
)


class UpdateOrderStatusUseCase:

    def __init__(
        self,
        repository: OrderRepository,
    ):
        self.repository = repository

    def execute(
        self,
        order_id: UUID,
        new_status: OrderStatus,
    ) -> Order:

        order = self.repository.get_by_id(
            order_id
        )

        if order is None:
            raise OrderNotFoundError(
                f"Order {order_id} not found"
            )

        if new_status == OrderStatus.PROCESSING:
            order.mark_as_processing()

        elif new_status == OrderStatus.SHIPPED:
            order.mark_as_shipped()

        elif new_status == OrderStatus.DELIVERED:
            order.mark_as_delivered()

        elif new_status == OrderStatus.CANCELLED:
            order.cancel()

        self.repository.update(order)

        return order