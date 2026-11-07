import uvicorn
from fastapi.middleware.cors import CORSMiddleware

from typing import TYPE_CHECKING, List
import fastapi as _fastapi
import sqlalchemy.orm as _orm

import schemas as _schemas
import services as _services

if TYPE_CHECKING:
    from sqlalchemy.orm import Session


app = _fastapi.FastAPI()

origins = [
    "http://localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    )

@app.post("/api/users/", response_model=_schemas.User)
async def create_user(user: _schemas.CreateUser,
                       db: _orm.Session = _fastapi.Depends(_services.get_db)
                       ):
    return await _services.create_user(user=user, db=db)

@app.get("/api/users/by-username/{user_name}", response_model=_schemas.User)
async def get_user_by_username(
        user_name: str,
        db: _orm.Session = _fastapi.Depends(_services.get_db)):
    user = await _services.get_user_by_username(user_name=user_name, db=db)
    if user is None:
        raise _fastapi.HTTPException(status_code=404, detail="User does not exist")
    return user

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

@app.get("/api/users/{user_id}/ingredients", response_model=List[str])
async def get_ingredients(user_id: int, db: _orm.Session = _fastapi.Depends(_services.get_db)):
    user = await _services.get_user(user_id=user_id, db=db)
    if user is None:
        raise _fastapi.HTTPException(status_code=404, detail="User does not exist")
    return user.ingredients

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

@app.put("/api/users/{user_id}/ingredients", response_model=_schemas.User)
async def update_ingredients(user_id: int,
                             ingredients: List[str],
                             db: _orm.Session = _fastapi.Depends(_services.get_db)):
    user = await _services.get_user(user_id=user_id, db=db)
    if user is None:
        raise _fastapi.HTTPException(status_code=404, detail="User does not exist")

    return await _services.update_ingredients(  user=user,
                                                newingredients=ingredients,
                                                db=db)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)