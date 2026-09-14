from unittest.mock import Mock
from uuid import uuid4

import pytest

from app.application.use_cases.get_order import GetOrderUseCase
from app.domain.exceptions.order_exceptions import (
    OrderNotFoundError,
)


def test_get_order_raises_exception_when_not_found():

    repository = Mock()

    repository.get_by_id.return_value = None

    use_case = GetOrderUseCase(repository)

    with pytest.raises(
        OrderNotFoundError
    ):
        use_case.execute(uuid4())