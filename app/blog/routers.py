from fastapi.requests import Request
from app.blog import services as svc

async def read_blog(request: Request):
    return await svc.BlogService(request).read_blog()
