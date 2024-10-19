from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from docker import DockerClient
from prometheus_client import make_asgi, Counter, Histogram

app = FastAPI()
templates = Jinja2Templates(directory="templates")


client = DockerClient(base_url='unix://var/run/docker.sock')

@app.get("/", response_class=HTMLResponse)
async def read_docker_data(request: Request):
  
    containers = client.containers.list()
   
    container_data = []
    for container in containers:
        container_info = {
            "name": container.name,
            "id": container.id,
            "status": container.status,
            "image": container.image.tags,
        }
        container_data.append(container_info)

    return templates.TemplateResponse("index.html", {"request": request, "containers": container_data})
