from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import FileResponse
# Load methods in current context to be called directly.
from .lib.utils import *

from app.routers import docker, kubernetes

app = FastAPI()


templates = Jinja2Templates(directory="templates")

app.mount("/assets", StaticFiles(directory="assets"), name="assets")

app.include_router(docker.router)
app.include_router(kubernetes.router)

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("render.html", {"request": request, "data": readFile("home.md")})


@app.get("/{page_name}", response_class=HTMLResponse)
async def redner_page(request: Request, page_name: str):
    return templates.TemplateResponse("render.html", {"request": request, "data": readFile(page_name+".md")})

@app.get("/tpl/{page_name}", response_class=HTMLResponse)
async def redner_tpl(request: Request, page_name: str):
     return FileResponse(path=os.path.join("generated/", page_name), filename=page_name, media_type='text/mp4')