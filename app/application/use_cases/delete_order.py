from uuid import UUID

from app.domain.exceptions.order_exceptions import (
    OrderNotFoundError,
)
from app.domain.repositories.order_repository import (
    OrderRepository,
)


class DeleteOrderUseCase:

    def __init__(
        self,
        repository: OrderRepository,
    ):
        self.repository = repository

    def execute(
        self,
        order_id: UUID,
    ) -> None:

        order = self.repository.get_by_id(
            order_id
        )

        if order is None:
            raise OrderNotFoundError(
                f"Order {order_id} not found"
            )

        self.repository.delete(order_id)