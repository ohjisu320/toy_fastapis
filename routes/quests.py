from fastapi import APIRouter
from starlette.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request
from databases.connections import Database
from models.quest_question import Question
from models.quest_answer import Answer
router = APIRouter()

templates = Jinja2Templates(directory="templates/")

# connection.py에서 정의한 Database 클래스를 사용하여 객체 생성
collection_question = Database(Question)
collection_answer = Database(Answer)

@router.get("/test")
async def test(request:Request):
    list_question = await collection_question.get_all() # Question 데이터 모두 가져오기
    list_answer = await collection_answer.get_all() # Answer 데이터 모두 가져오기
    return templates.TemplateResponse(name="quests/test.html"
                                      , context={'request':request,
                                                 "list_question":list_question,
                                                 "list_answer":list_answer})
