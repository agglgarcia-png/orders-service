from app.api.routers.health import router as health_router
from app.api.routers.orders import router as orders_router
from app.domain.exceptions.order_exceptions import (
    CustomerRequiredError,
    InvalidOrderAmountError,
    InvalidOrderStatusTransitionError,
    OrderNotFoundError,
)
from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI(
    title="Orders Service",
    description="Orders API built with FastAPI and Hexagonal Architecture",
    version="1.0.0",
)


@app.exception_handler(OrderNotFoundError)
async def order_not_found_handler(
    request,
    exc: OrderNotFoundError,
):
    return JSONResponse(
        status_code=404,
        content={
            "message": str(exc)
        },
    )


@app.exception_handler(CustomerRequiredError)
async def customer_required_handler(
    request,
    exc: CustomerRequiredError,
):
    return JSONResponse(
        status_code=400,
        content={
            "message": str(exc)
        },
    )


@app.exception_handler(InvalidOrderAmountError)
async def invalid_amount_handler(
    request,
    exc: InvalidOrderAmountError,
):
    return JSONResponse(
        status_code=400,
        content={
            "message": str(exc)
        },
    )


@app.exception_handler(
    InvalidOrderStatusTransitionError
)
async def invalid_status_handler(
    request,
    exc: InvalidOrderStatusTransitionError,
):
    return JSONResponse(
        status_code=400,
        content={
            "message": str(exc)
        },
    )


app.include_router(health_router)

app.include_router(orders_router)