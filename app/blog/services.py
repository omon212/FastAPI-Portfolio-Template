from app.base.services import BaseService, templates

class BlogService(BaseService):

    async def read_blog(self):
        return templates.TemplateResponse("blog.html", {"request": self.request})
