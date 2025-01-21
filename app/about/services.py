from app.base.services import BaseService,templates


class AboutService(BaseService):

    async def read_about(self):
        return templates.TemplateResponse("about.html",{"request":self.request})