from fastapi import FastAPI
from app.base import services as base_services
from app.home import routers as home_routers
from app.blog import routers as blogs_routers
from app.about import routers as about_routers
app = FastAPI()

app.mount("/static", base_services.static_files, name='static')


app.add_route("/home", home_routers.read_home, methods=["GET"])
app.add_route("/", home_routers.read_home, methods=["GET"])
app.add_route("/blog", blogs_routers.read_blog, methods=["GET"])
app.add_route("/about", about_routers.read_about, methods=["GET"])

