"""API router for health-related operations."""

from fastapi import APIRouter

router = APIRouter(prefix="/health", tags=["Health"])


@router.get("/liveness")
async def get_liveness() -> dict[str, str]:
    """Get liveness status of the service.

    Returns:
        A dictionary indicating the liveness status.
    """
    return {"message": "I'm alive"}


@router.get("/readiness")
async def get_readiness() -> dict[str, str]:
    """Get readiness status of the service.

    Returns:
        A dictionary indicating the readiness status.
    """
    return {"message": "I'm ready"}
