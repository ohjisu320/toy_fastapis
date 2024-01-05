from fastapi import FastAPI
app = FastAPI()

from databases.connections import Settings
settings = Settings()

@app.on_event("startup")
async def init_db() : 
    await settings.initialize_database()
    # database의 세팅을 바꾸면 한번씩 재실행 시켜줘야 함.
from fastapi import Request
from fastapi.templating import Jinja2Templates
from routes.quests import router as quests_router

app.include_router(quests_router, prefix="/quest")




# html 들이 있는 폴더 위치
templates = Jinja2Templates(directory="templates/")

from fastapi.middleware.cors import CORSMiddleware
# No 'Access-Control-Allow-Origin'
# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 실제 운영 환경에서는 접근 가능한 도메인만 허용하는 것이 좋습니다.
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root(request:Request):
    # return {"message": "jisu World"}
    return templates.TemplateResponse("quest_main.html",{'request':Request})


