from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/api")


class HealthcheckResponse(BaseModel):
    ok: bool


@router.get("/healthcheck", response_model=HealthcheckResponse)
async def healthcheck() -> HealthcheckResponse:
    return HealthcheckResponse(ok=True)
