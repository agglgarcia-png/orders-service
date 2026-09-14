from datetime import UTC, datetime

from fastapi import APIRouter, status

router = APIRouter(
    tags=["Health"],
)


@router.get(
    "/health",
    status_code=status.HTTP_200_OK,
    summary="Health Check",
    description="Verifica que el servicio esté disponible.",
)
def health():
    return {
        "status": "ok",
        "service": "orders-service",
        "version": "1.0.0",
        "timestamp": datetime.now(UTC).isoformat(),
    }