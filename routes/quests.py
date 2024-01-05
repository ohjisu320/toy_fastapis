from fastapi import APIRouter
from starlette.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request


router = APIRouter()

templates = Jinja2Templates(directory="templates/")

@router.get("/create", response_class=HTMLResponse)
async def forms(request:Request):
    return templates.TemplateResponse(name="quests/create.html", context={'request':request})

@router.get("/result", response_class=HTMLResponse)
async def forms(request:Request):
    return templates.TemplateResponse(name="quests/result.html", context={'request':request})

@router.get("/test", response_class=HTMLResponse)
async def forms(request:Request):
    return templates.TemplateResponse(name="quests/test.html", context={'request':request})