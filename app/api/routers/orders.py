from uuid import UUID

from fastapi import APIRouter, Depends, status

from app.api.dependencies import (
    get_create_order_use_case,
    get_delete_order_use_case,
    get_get_order_use_case,
    get_update_order_status_use_case,
)
from app.api.schemas.order import (
    CreateOrderRequest,
    OrderResponse,
    UpdateOrderStatusRequest,
)
from app.application.use_cases.create_order import (
    CreateOrderUseCase,
)
from app.application.use_cases.delete_order import (
    DeleteOrderUseCase,
)
from app.application.use_cases.get_order import (
    GetOrderUseCase,
)
from app.application.use_cases.update_order_status import (
    UpdateOrderStatusUseCase,
)

router = APIRouter(
    prefix="/orders",
    tags=["Orders"],
)


@router.post(
    "",
    response_model=OrderResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_order(
    request: CreateOrderRequest,
    use_case: CreateOrderUseCase = Depends(
        get_create_order_use_case,
    ),
):

    order = use_case.execute(
        customer_id=request.customer_id,
        total_amount=request.total_amount,
    )

    return OrderResponse(
        id=order.id,
        customer_id=order.customer_id,
        total_amount=order.total_amount,
        status=order.status.value,
        created_at=order.created_at,
        updated_at=order.updated_at,
    )


@router.get(
    "/{order_id}",
    response_model=OrderResponse,
)
def get_order(
    order_id: UUID,
    use_case: GetOrderUseCase = Depends(
        get_get_order_use_case,
    ),
):

    order = use_case.execute(order_id)

    return OrderResponse(
        id=order.id,
        customer_id=order.customer_id,
        total_amount=order.total_amount,
        status=order.status.value,
        created_at=order.created_at,
        updated_at=order.updated_at,
    )


@router.patch(
    "/{order_id}/status",
    response_model=OrderResponse,
)
def update_order_status(
    order_id: UUID,
    request: UpdateOrderStatusRequest,
    use_case: UpdateOrderStatusUseCase = Depends(
        get_update_order_status_use_case,
    ),
):

    order = use_case.execute(
        order_id=order_id,
        new_status=request.status,
    )

    return OrderResponse(
        id=order.id,
        customer_id=order.customer_id,
        total_amount=order.total_amount,
        status=order.status.value,
        created_at=order.created_at,
        updated_at=order.updated_at,
    )


@router.delete(
    "/{order_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_order(
    order_id: UUID,
    use_case: DeleteOrderUseCase = Depends(
        get_delete_order_use_case,
    ),
):

    use_case.execute(order_id)

