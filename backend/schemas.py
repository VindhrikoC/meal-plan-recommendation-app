import datetime as _dt
import pydantic as _pydantic
from typing import List

class _BaseUser(_pydantic.BaseModel):
    user_name: str
    ingredients: List[str] = _pydantic.Field(default_factory=list)

class User(_BaseUser):
    id: int
    date_created: _dt.datetime

    class Config:
        orm_mode = True
        from_attributes = True

class CreateUser(_BaseUser):
    pass