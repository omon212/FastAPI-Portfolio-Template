from fastapi.requests import Request
from app.about import services as svc


async def read_about(request: Request):
    return await svc.AboutService(request).read_about()
