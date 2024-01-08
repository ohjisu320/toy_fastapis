from fastapi import APIRouter
from starlette.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request
from databases.connections import Database
from models.quest_question import Question
from models.quest_answer import Answer
router = APIRouter()

templates = Jinja2Templates(directory="templates/")
collection_question = Database(Question)
collection_answer = Database(Answer)
# @router.get("/create", response_class=HTMLResponse)
# async def create(request:Request):
#   collection_question = Database(Question)
#   collection_answer = Database(Answer)
#   list_question = await collection_question.get_all()
#   list_answer = await collection_answer.get_all()
#   return templates.TemplateResponse(name="quests/create.html", context={'request':request,
#                                                                           'list_question' : list_question,
#                                                                           'list_answer' : list_answer
#                                                                           })

@router.post("/result", response_class=HTMLResponse)
async def result_post(request:Request):
  user_dict = await dict(request.form())

  return templates.TemplateResponse(name="quests/result.html", context={'request':request})
@router.get("/result", response_class=HTMLResponse)
async def result_get(request:Request):

  list_user = [
    {
    "응시자": "오지수",
    "응시자정답": [3,1,3,1,3],
    "응시자점수": 100
  },
    {
    "응시자": "서정민",
    "응시자정답": [3,1,3,1,3],
    "응시자점수": 100
  },
    {
    "응시자": "김명준",
    "응시자정답": [3,1,3,1,3],
    "응시자점수": 100
  }
]
  return templates.TemplateResponse(name="quests/result.html", context={'request':request,
                                                                          'list_user' : list_user})

@router.get("/test")
async def test(request:Request):
  list_question = await collection_question.get_all()
  pass
  list_answer = await collection_answer.get_all()
  pass
  return templates.TemplateResponse(name="quests/test.html", context={'request':request,"list_question":list_question,"list_answer":list_answer})


# @router.post("/create", response_class=HTMLResponse)
# async def create(request:Request):
#     return templates.TemplateResponse(name="quests/create.html", context={'request':request})


# @router.post("/test", response_class=HTMLResponse)
# async def test(request:Request):
#     return templates.TemplateResponse(name="quests/test.html", context={'request':request})