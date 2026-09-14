from uuid import UUID

from app.domain.entities.order import Order
from app.domain.exceptions.order_exceptions import (
    OrderNotFoundError,
)
from app.domain.repositories.order_repository import OrderRepository


class GetOrderUseCase:

    def __init__(
        self,
        repository: OrderRepository
    ):
        self.repository = repository

    def execute(
        self,
        order_id: UUID
    ) -> Order:

        order = self.repository.get_by_id(
            order_id
        )

        if order is None:
            raise OrderNotFoundError(
                f"Order {order_id} not found"
            )

        return order