import datetime as _dt
import pydantic as _pydantic

class _BaseUser(_pydantic.BaseModel):
    user_name: str

class User(_BaseUser):
    id: int
    date_created: _dt.datetime

    class Config:
        orm_mode = True
        from_attributes = True

class CreateUser(_BaseUser):
    pass