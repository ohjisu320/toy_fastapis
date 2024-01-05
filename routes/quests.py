from fastapi import APIRouter
from starlette.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request


router = APIRouter()

templates = Jinja2Templates(directory="templates/")

@router.get("/create", response_class=HTMLResponse)
async def create(request:Request):
    return templates.TemplateResponse(name="quests/create.html", context={'request':request})

@router.get("/result", response_class=HTMLResponse)
async def result(request:Request):
    return templates.TemplateResponse(name="quests/result.html", context={'request':request})

list_question =[
  {
    "질문": "세계에서 가장 큰 강은 어디일까요?",
    "정답": "3",
    "점수": 10
  },
  {
    "질문": "다음 중 최초의 인공위성은 무엇일까요?",
    "정답": "1",
    "점수": 8
  },
  {
    "질문": "태양계에서 가장 큰 행성은 무엇일까요?",
    "정답": "3",
    "점수": 9
  },
  {
    "질문": "삼국지에서 유비, 관우, 장비가 소속한 나라는 어디일까요?",
    "정답": "1",
    "점수": 7
  },
  {
    "질문": "다음 중 유럽에 위치한 나라는 어디일까요?",
    "정답": "3",
    "점수": 6
  }
]


@router.get("/test", response_class=HTMLResponse, )
async def test(request:Request):
    list_question =[
  {
    "질문": "세계에서 가장 큰 강은 어디일까요?",
    "정답": "3",
    "점수": 10
  },
  {
    "질문": "다음 중 최초의 인공위성은 무엇일까요?",
    "정답": "1",
    "점수": 8
  },
  {
    "질문": "태양계에서 가장 큰 행성은 무엇일까요?",
    "정답": "3",
    "점수": 9
  },
  {
    "질문": "삼국지에서 유비, 관우, 장비가 소속한 나라는 어디일까요?",
    "정답": "1",
    "점수": 7
  },
  {
    "질문": "다음 중 유럽에 위치한 나라는 어디일까요?",
    "정답": "3",
    "점수": 6
  }
]
    list_answer = [
    {"답안": "아마존 강"},
    {"답안": "단데 강"},
    {"답안": "나일 강"},
    {"답안": "미시시피 강"},
    {"답안": "스푸트니크 1호"},
    {"답안": "아리랑 1호"},
    {"답안": "텔레스타 1호"},
    {"답안": "광명성 1호"},
    {"답안": "지구"},
    {"답안": "토성"},
    {"답안": "목성"},
    {"답안": "화성"},
    {"답안": "위나라"},
    {"답안": "우나라"},
    {"답안": "신라"},
    {"답안": "촉나라"},
    {"답안": "아르헨티나"},
    {"답안": "중국"},
    {"답안": "독일"},
    {"답안": "나이지리아"}
]
    

    return templates.TemplateResponse(name="quests/test.html", context={'request':request,
                                                                        'list_question': list_question,
                                                                        'list_answer':list_answer})


@router.post("/create", response_class=HTMLResponse)
async def create(request:Request):
    return templates.TemplateResponse(name="quests/create.html", context={'request':request})

@router.post("/result", response_class=HTMLResponse)
async def result(request:Request):
    return templates.TemplateResponse(name="quests/result.html", context={'request':request})

@router.post("/test", response_class=HTMLResponse)
async def test(request:Request):
    return templates.TemplateResponse(name="quests/test.html", context={'request':request})