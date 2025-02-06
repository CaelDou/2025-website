from fastapi import FastAPI, Request
from starlette.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="static")

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    context = {"request": request}
    return templates.TemplateResponse("/index.html", context)

