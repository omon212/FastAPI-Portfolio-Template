from fastapi.requests import Request
from app.home import services as svc


async def read_home(request: Request):
    return await svc.HomeService(request).read_home()
