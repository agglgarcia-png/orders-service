from datetime import UTC, datetime
from decimal import Decimal
from uuid import uuid4

from fastapi.testclient import TestClient

from app.api.dependencies import (
    get_create_order_use_case,
    get_delete_order_use_case,
    get_get_order_use_case,
    get_update_order_status_use_case,
)
from app.domain.entities.order import Order
from app.domain.value_objects.order_status import (
    OrderStatus,
)
from app.main import app

client = TestClient(app)


def build_order():

    now = datetime.now(UTC)

    return Order(
        id=uuid4(),
        customer_id="CLIENT-001",
        total_amount=Decimal("100.00"),
        status=OrderStatus.PENDING,
        created_at=now,
        updated_at=now,
    )


def test_create_order():

    order = build_order()

    class FakeCreateOrderUseCase:

        def execute(
            self,
            customer_id,
            total_amount,
        ):
            return order

    app.dependency_overrides[
        get_create_order_use_case
    ] = lambda: FakeCreateOrderUseCase()

    response = client.post(
        "/orders",
        json={
            "customer_id": "CLIENT-001",
            "total_amount": "100.00",
        },
    )

    assert response.status_code == 201

    data = response.json()

    assert data["customer_id"] == "CLIENT-001"
    assert data["status"] == "PENDING"

    app.dependency_overrides.clear()


def test_get_order():

    order = build_order()

    class FakeGetOrderUseCase:

        def execute(self, order_id):
            return order

    app.dependency_overrides[
        get_get_order_use_case
    ] = lambda: FakeGetOrderUseCase()

    response = client.get(
        f"/orders/{order.id}"
    )

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == str(order.id)

    app.dependency_overrides.clear()


def test_update_order_status():

    order = build_order()

    order.status = OrderStatus.PROCESSING

    class FakeUpdateOrderStatusUseCase:

        def execute(
            self,
            order_id,
            new_status,
        ):
            return order

    app.dependency_overrides[
        get_update_order_status_use_case
    ] = lambda: FakeUpdateOrderStatusUseCase()

    response = client.patch(
        f"/orders/{order.id}/status",
        json={
            "status": "PROCESSING"
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert data["status"] == "PROCESSING"

    app.dependency_overrides.clear()


def test_delete_order():

    class FakeDeleteOrderUseCase:

        def execute(self, order_id):
            return None

    app.dependency_overrides[
        get_delete_order_use_case
    ] = lambda: FakeDeleteOrderUseCase()

    response = client.delete(
        f"/orders/{uuid4()}"
    )

    assert response.status_code == 204

    app.dependency_overrides.clear()