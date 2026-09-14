from unittest.mock import Mock
from uuid import uuid4

import pytest

from app.application.use_cases.delete_order import (
    DeleteOrderUseCase,
)
from app.domain.exceptions.order_exceptions import (
    OrderNotFoundError,
)


def test_delete_order_raises_error_when_order_not_found():

    repository = Mock()

    repository.get_by_id.return_value = None

    use_case = DeleteOrderUseCase(
        repository
    )

    with pytest.raises(
        OrderNotFoundError
    ):
        use_case.execute(
            uuid4()
        )