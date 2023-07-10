from fastapi import Request, Form, APIRouter
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import os

router = APIRouter()
templates = Jinja2Templates(directory="templates/")


@router.get("/docker", response_class=HTMLResponse)
def form_get(request: Request):
    result = "Type a number"
    return templates.TemplateResponse('docker.html', context={'request': request, 'result': result})

@router.post("/dockerize", response_class=HTMLResponse)
def form_dockerize(request: Request, application: str = Form(...), port: int = Form(...)):
    result = "Application type is {} and port is {} ".format(application, port)
    cmd = ""
    fileLink = generate_dockerfile(application, port, cmd)
    return templates.TemplateResponse(
        'docker.html',
        context={'request': request, 'result': result, 'fileLink': fileLink})

def generate_dockerfile(application, port, cmd):
    filepath = os.path.join("generated/", application +"_Dockerfile")
    with open(filepath, "r", encoding="utf-8") as textFile:
        fileText = textFile.read()
  
    text = fileText.replace("REPL_PORT", str(port))
    with open(os.path.join("generated/", "Dockerfile"), "w") as w:
        w.write(text)
    return "Dockerfile"

@router.post("/sum2", response_class=HTMLResponse)
def sum(request: Request, num: int = Form(...)):
    return templates.TemplateResponse('twoforms.html', context={'request': request, 'result': num +2, 'usernum': num})
