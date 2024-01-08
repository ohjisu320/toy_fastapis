from typing import Any, List, Optional
from beanie import init_beanie, PydanticObjectId
from models.users import User
from models.quest_answer import Answer
from models.quest_question import Question

from motor.motor_asyncio import AsyncIOMotorClient
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL : Optional[str]

    async def initialize_database(self,):
        client = AsyncIOMotorClient(self.DATABASE_URL)
        await init_beanie(database=client.get_default_database(),
                          document_models=[User, Question, Answer])

    class Config:
        env_file = ".env"

class Database:
    # model == db-collection
    def __init__(self, model) -> None:
        self.model = model
        pass

    # 전체 list
    async def get_all(self) :
        documents = await self.model.find_all().to_list() # find({})
        pass
        return documents
    
    # 상세 보기
    async def get(self, id: PydanticObjectId) -> Any:
        doc = await self.model.get(id) # find_one
        if doc:
            return doc
        return False
    
    # 저장
    async def save(self, document) -> None:
        await document.create()
        return None