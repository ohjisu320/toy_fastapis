from typing import Optional, List

from beanie import Document, Link
from pydantic import BaseModel, EmailStr

# 개발자 실수로 들어가는 field 제한
class User(Document):
    # name = None datatype을 알 수 없음.
    name: Optional[str] = None # Optional은 넣어도 되고 안넣어도 된다고 지정해주는 기능.
    email: Optional[EmailStr] = None
    pswd: Optional[str] = None
    manager: Optional[str] = None
    sellist1 : Optional[str] = None
    text : Optional[str] = None
  
    class Settings:
        name = "users"
  