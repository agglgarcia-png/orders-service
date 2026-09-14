from decimal import Decimal
from unittest.mock import Mock

from app.application.use_cases.create_order import CreateOrderUseCase
from app.domain.value_objects.order_status import OrderStatus


def test_create_order_saves_order_in_repository():

    repository = Mock()

    use_case = CreateOrderUseCase(repository)

    order = use_case.execute(
        customer_id="CLIENT-001",
        total_amount=Decimal("150.50")
    )

    repository.save.assert_called_once()

    saved_order = repository.save.call_args[0][0]

    assert saved_order.customer_id == "CLIENT-001"
    assert saved_order.total_amount == Decimal("150.50")
    assert saved_order.status == OrderStatus.PENDING

    assert order.id == saved_order.id