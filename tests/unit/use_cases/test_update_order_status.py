from unittest.mock import Mock
from uuid import uuid4

import pytest

from app.application.use_cases.update_order_status import (
    UpdateOrderStatusUseCase,
)
from app.domain.exceptions.order_exceptions import (
    OrderNotFoundError,
)
from app.domain.value_objects.order_status import (
    OrderStatus,
)


def test_update_to_processing():

    repository = Mock()
    order = Mock()

    repository.get_by_id.return_value = order

    use_case = UpdateOrderStatusUseCase(repository)

    result = use_case.execute(
        uuid4(),
        OrderStatus.PROCESSING,
    )

    order.mark_as_processing.assert_called_once()

    repository.update.assert_called_once_with(
        order
    )

    assert result == order


def test_update_to_shipped():

    repository = Mock()
    order = Mock()

    repository.get_by_id.return_value = order

    use_case = UpdateOrderStatusUseCase(repository)

    result = use_case.execute(
        uuid4(),
        OrderStatus.SHIPPED,
    )

    order.mark_as_shipped.assert_called_once()

    repository.update.assert_called_once_with(
        order
    )

    assert result == order


def test_update_to_delivered():

    repository = Mock()
    order = Mock()

    repository.get_by_id.return_value = order

    use_case = UpdateOrderStatusUseCase(repository)

    result = use_case.execute(
        uuid4(),
        OrderStatus.DELIVERED,
    )

    order.mark_as_delivered.assert_called_once()

    repository.update.assert_called_once_with(
        order
    )

    assert result == order


def test_update_to_cancelled():

    repository = Mock()
    order = Mock()

    repository.get_by_id.return_value = order

    use_case = UpdateOrderStatusUseCase(repository)

    result = use_case.execute(
        uuid4(),
        OrderStatus.CANCELLED,
    )

    order.cancel.assert_called_once()

    repository.update.assert_called_once_with(
        order
    )

    assert result == order


def test_update_order_status_raises_error_when_order_not_found():

    repository = Mock()

    repository.get_by_id.return_value = None

    use_case = UpdateOrderStatusUseCase(repository)

    with pytest.raises(
        OrderNotFoundError
    ):
        use_case.execute(
            uuid4(),
            OrderStatus.PROCESSING,
        )