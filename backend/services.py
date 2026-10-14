from typing import TYPE_CHECKING, List

import database as _database
import models as _models
import schemas as _schemas

if TYPE_CHECKING:
    from sqlalchemy.orm import Session

def _add_tables():
    return _database.Base.metadata.create_all(bind=_database.engine)

def get_db():
    db = _database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

async def create_user(user: _schemas.CreateUser, db: "Session"
                      ) -> _schemas.User:
    user = _models.User(**user.dict())
    db.add(user)
    db.commit()
    db.refresh(user)
    return _schemas.User.from_orm(user)

async def get_all_users(db: "Session") -> List[_schemas.User]:
    users = db.query(_models.User).all()
    return list(map(_schemas.User.from_orm, users))

async def get_user(user_id: int, db: "Session"):
    user = db.query(_models.User).filter(_models.User.id == user_id).first()
    return user

async def delete_user(user: _models.User, db:"Session"):
    db.delete(user)
    db.commit()

async def update_user(user_data: _schemas.CreateUser,
                       user: _models.User,
                         db: "Session") -> _schemas.User:
    user.user_name = user_data.user_name
    db.commit()
    db.refresh(user)

    return _schemas.User.from_orm(user)