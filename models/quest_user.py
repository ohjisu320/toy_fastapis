from typing import Optional, List

from beanie import Document, Link
from pydantic import BaseModel, EmailStr

# 개발자 실수로 들어가는 field 제한
class Quest_user(Document):
    
    User_name: Optional[str] = None # Optional은 넣어도 되고 안넣어도 된다고 지정해주는 기능.
    answer1: Optional[str] = None
    answer2: Optional[str] = None
    answer3: Optional[str] = None
    answer4: Optional[str] = None
    answer5: Optional[str] = None

    class Settings:
        name = "quest_user"
  