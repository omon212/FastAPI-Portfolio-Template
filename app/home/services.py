from app.base.services import BaseService, templates

class HomeService(BaseService):

    async def read_home(self):
        return templates.TemplateResponse("home.html", {"request": self.request})

