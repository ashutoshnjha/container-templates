from fastapi import FastAPI, Request, Form, APIRouter
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import os

router = APIRouter()
templates = Jinja2Templates(directory="templates/")


@router.get("/kubernetes", response_class=HTMLResponse)
def form_get(request: Request):
    key = os.getenv("unsplash_key")
    print(key)
    result = "Type a number"
    return templates.TemplateResponse('kubernetes.html', context={'request': request, 'result': result})

@router.post("/kubefile", response_class=HTMLResponse)
def form_dockerize(request: Request, 
                   image: str = Form(...),
                   app_name: str = Form(...), 
                   container_name: str = Form(...),
                   port: int = Form(...),
                   nodePort: int = Form(...),
                   targetPort: int = Form(...)):
    result = "Container image is {} and port is {} ".format(image, port)
    fileLink = generate_kubefile(image, app_name,container_name, port, nodePort, targetPort)
    return templates.TemplateResponse(
        'kubernetes.html',
        context={'request': request, 'result': result, 'fileLink': fileLink})

def generate_kubefile(image, app_name,container_name, port, nodePort, targetPort):
    application =""
    filepath = os.path.join("generated/", application +"kubefile")
    with open(filepath, "r", encoding="utf-8") as textFile:
        fileText = textFile.read()
  
    text = fileText.replace("REPL_PORT", str(port))
    text = text.replace("REPL_APP_NAME", str(app_name))
    text = text.replace("REPL_IMAGE", str(image))
    text = text.replace("REPL_CONTAINER_NAME", str(container_name))
    text = text.replace("REPL_NODE_PORT", str(nodePort))
    text = text.replace("REPL_TARGET_PORT", str(targetPort))
    with open(os.path.join("generated/", "kubeservice.yaml"), "w") as w:
        w.write(text)
    return "kubeservice.yaml"
