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
from app.infrastructure.database.session import (
    SessionLocal,
)
from app.infrastructure.repositories.sql_order_repository import (
    SqlOrderRepository,
)
from fastapi import Depends
from sqlalchemy.orm import Session


def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


def get_order_repository(
    db: Session = Depends(get_db),
):

    return SqlOrderRepository(db)


def get_create_order_use_case(
    repository=Depends(
        get_order_repository
    ),
):

    return CreateOrderUseCase(
        repository
    )


def get_get_order_use_case(
    repository=Depends(
        get_order_repository
    ),
):

    return GetOrderUseCase(
        repository
    )


def get_update_order_status_use_case(
    repository=Depends(
        get_order_repository
    ),
):

    return UpdateOrderStatusUseCase(
        repository
    )


def get_delete_order_use_case(
    repository=Depends(
        get_order_repository
    ),
):

    return DeleteOrderUseCase(
        repository
    )