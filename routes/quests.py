from fastapi import FastAPI, Request, APIRouter
from starlette.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic_settings import BaseSettings
from fastapi.responses import RedirectResponse

# 환경 변수 로드를 위한 Settings 클래스 정의
class Settings(BaseSettings):
    database_url: str  # MongoDB의 전체 URL을 기대합니다.

    class Config:
        env_file = ".env"

# 설정 로드
settings = Settings()

# FastAPI 앱과 라우터 초기화
app = FastAPI()
router = APIRouter()

# Motor 클라이언트 및 데이터베이스 설정
client = AsyncIOMotorClient(settings.database_url)
db = client.get_default_database()

# Jinja2 템플릿 설정
templates = Jinja2Templates(directory="templates")

# MongoDB 컬렉션 설정
question_collection = db['quest_question']
answer_collection = db['quest_answer']
user_collection = db['quest_user']

# 데이터베이스 헬퍼 클래스
class Database:
    def __init__(self, collection):
        self.collection = collection

    async def get_all(self):
        return await self.collection.find().to_list(None)
        
    # 저장
    async def save(self, document) -> None:
        await document.create()
        return None

# 퀴즈 경로
@router.get("/test", response_class=HTMLResponse)
async def get_quiz(request: Request):
    db = Database(question_collection)
    quiz_list = await db.get_all()
    db = Database(answer_collection)
    quiz_answer = await db.get_all()
    return templates.TemplateResponse("/quests/test.html", 
        {"request": request,
        "Quiz_list": quiz_list,
        "Quiz_answer": quiz_answer
    })

@router.post("/result")
async def submit_quiz(request: Request):
    form_data = await request.form()
    db = Database(user_collection)
    db.save(**form_data)
    # # 응시자 이름
    # name = form_data.get('name')
    
    # # 응시자 답변을 리스트로 만들기
    # answers = [form_data.get(f'answer{i}') for i in range(4)]
    
    # data = {'응시자': name, '응시자정답': answers, '응시자점수': 0}  # 점수는 임시로 0으로 설정
    await db.insert(data)
    return templates.TemplateResponse("/quests/test.html", {"request": request,"Quiz_list": quiz_list,"Quiz_answer": quiz_answer
    })
# 라우터 등록
app.include_router(router, prefix='/quest')

# 애플리케이션 실행
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
