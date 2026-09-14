from datetime import UTC, datetime
from decimal import Decimal
from uuid import uuid4

import pytest

from app.domain.entities.order import Order
from app.domain.exceptions.order_exceptions import (
    CustomerRequiredError,
    InvalidOrderAmountError,
    InvalidOrderStatusTransitionError,
)
from app.domain.value_objects.order_status import (
    OrderStatus,
)


def create_order(status=OrderStatus.PENDING):

    now = datetime.now(UTC)

    return Order(
        id=uuid4(),
        customer_id="CLIENT-001",
        total_amount=Decimal("100.00"),
        status=status,
        created_at=now,
        updated_at=now,
    )


def test_create_order_successfully():

    order = create_order()

    assert order.customer_id == "CLIENT-001"
    assert order.total_amount == Decimal("100.00")
    assert order.status == OrderStatus.PENDING


def test_customer_id_is_required():

    with pytest.raises(CustomerRequiredError):

        Order(
            id=uuid4(),
            customer_id="",
            total_amount=Decimal("100.00"),
            status=OrderStatus.PENDING,
            created_at=datetime.now(UTC),
            updated_at=datetime.now(UTC),
        )


def test_order_amount_must_be_greater_than_zero():

    with pytest.raises(
        InvalidOrderAmountError
    ):

        Order(
            id=uuid4(),
            customer_id="CLIENT-001",
            total_amount=Decimal(0),
            status=OrderStatus.PENDING,
            created_at=datetime.now(UTC),
            updated_at=datetime.now(UTC),
        )


def test_mark_as_processing():

    order = create_order()

    order.mark_as_processing()

    assert order.status == OrderStatus.PROCESSING


def test_mark_as_processing_invalid_transition():

    order = create_order(
        OrderStatus.SHIPPED
    )

    with pytest.raises(
        InvalidOrderStatusTransitionError
    ):
        order.mark_as_processing()


def test_mark_as_shipped():

    order = create_order(
        OrderStatus.PROCESSING
    )

    order.mark_as_shipped()

    assert order.status == OrderStatus.SHIPPED


def test_mark_as_shipped_invalid_transition():

    order = create_order(
        OrderStatus.PENDING
    )

    with pytest.raises(
        InvalidOrderStatusTransitionError
    ):
        order.mark_as_shipped()


def test_mark_as_delivered():

    order = create_order(
        OrderStatus.SHIPPED
    )

    order.mark_as_delivered()

    assert order.status == OrderStatus.DELIVERED


def test_mark_as_delivered_invalid_transition():

    order = create_order(
        OrderStatus.PROCESSING
    )

    with pytest.raises(
        InvalidOrderStatusTransitionError
    ):
        order.mark_as_delivered()


def test_cancel_order():

    order = create_order(
        OrderStatus.PROCESSING
    )

    order.cancel()

    assert order.status == OrderStatus.CANCELLED


def test_cancel_delivered_order():

    order = create_order(
        OrderStatus.DELIVERED
    )

    with pytest.raises(
        InvalidOrderStatusTransitionError
    ):
        order.cancel()


def test_cancel_cancelled_order():

    order = create_order(
        OrderStatus.CANCELLED
    )

    with pytest.raises(
        InvalidOrderStatusTransitionError
    ):
        order.cancel()