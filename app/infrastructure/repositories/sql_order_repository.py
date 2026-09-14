from uuid import UUID

from app.domain.entities.order import Order
from app.domain.repositories.order_repository import (
    OrderRepository,
)
from app.domain.value_objects.order_status import (
    OrderStatus,
)
from app.infrastructure.database.models import (
    OrderModel,
)


class SqlOrderRepository(OrderRepository):

    def __init__(self, session):
        self.session = session

    def save(self, order: Order) -> None:

        db_order = OrderModel(
            id=str(order.id),
            customer_id=order.customer_id,
            total_amount=order.total_amount,
            status=order.status.value,
            created_at=order.created_at,
            updated_at=order.updated_at,
        )

        self.session.add(db_order)
        self.session.commit()

    def get_by_id(
        self,
        order_id: UUID,
    ) -> Order | None:

        db_order = (
            self.session.query(OrderModel)
            .filter_by(id=str(order_id))
            .first()
        )

        if db_order is None:
            return None

        return Order(
            id=UUID(db_order.id),
            customer_id=db_order.customer_id,
            total_amount=db_order.total_amount,
            status=OrderStatus(db_order.status),
            created_at=db_order.created_at,
            updated_at=db_order.updated_at,
        )

    def update(
        self,
        order: Order,
    ) -> None:

        db_order = (
            self.session.query(OrderModel)
            .filter_by(id=str(order.id))
            .first()
        )

        if db_order is None:
            return

        db_order.customer_id = order.customer_id
        db_order.total_amount = order.total_amount
        db_order.status = order.status.value
        db_order.updated_at = order.updated_at

        self.session.commit()

    def delete(
        self,
        order_id: UUID,
    ) -> None:

        db_order = (
            self.session.query(OrderModel)
            .filter_by(id=str(order_id))
            .first()
        )

        if db_order is not None:
            self.session.delete(db_order)
            self.session.commit()