import requests
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/api")


class HealthcheckResponse(BaseModel):
    ok: bool


@router.get("/healthcheck", response_model=HealthcheckResponse)
async def healthcheck() -> HealthcheckResponse:
    return HealthcheckResponse(ok=True)


class Request(BaseModel):
    text: str


@router.post("/test")
async def test(request: Request):
    response = requests.post("http://embed:8080/embed", data={"inputs": request.text})
    print(response)
    return {"ok": True}
