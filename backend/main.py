from typing import TYPE_CHECKING, List
import fastapi as _fastapi
import sqlalchemy.orm as _orm

import schemas as _schemas
import services as _services

if TYPE_CHECKING:
    from sqlalchemy.orm import Session


app = _fastapi.FastAPI()

@app.post("/api/users/", response_model=_schemas.User)
async def create_user(user: _schemas.CreateUser,
                       db: _orm.Session = _fastapi.Depends(_services.get_db)
                       ):
    return await _services.create_user(user=user, db=db)

@app.get("/api/users/", response_model=List[_schemas.User])
async def get_users(db: _orm.Session = _fastapi.Depends(_services.get_db)):
    return await _services.get_all_users(db=db)

@app.get("/api/users/{user_id}", response_model=_schemas.User)
async def get_user(user_id: int,db: _orm.Session = _fastapi.Depends(_services.get_db)
                    ):
    user = await _services.get_user(user_id=user_id, db=db)
    if user is None:
        raise _fastapi.HTTPException(status_code=404, detail="User does not exist")
    
    return user

@app.delete("/api/users/{user_id}")
async def delete_user(user_id: int, db: _orm.Session = _fastapi.Depends(_services.get_db)):
    user = await _services.get_user(user_id=user_id, db=db)
    if user is None:
        raise _fastapi.HTTPException(status_code=404, detail="User does not exist")
    await _services.delete_user(user, db=db)

    return "Successfully deleted user {}".format(user_id)

@app.put("/api/users/{user_id}", response_model=_schemas.User)
async def update_user(user_id: int,
                      user_data: _schemas.CreateUser,
                      db: _orm.Session = _fastapi.Depends(_services.get_db)):
    user = await _services.get_user(user_id=user_id, db=db)
    if user is None:
        raise _fastapi.HTTPException(status_code=404, detail="User does not exist")

    return await _services.update_user(user_data=user_data,
                                       user=user,
                                       db=db)