# app/routers/admin.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..dependencies import get_db, check_admin
from ..schemas import user as user_schemas
from ..models import user

router = APIRouter(tags=['Admin'])


@router.get("/admin/users", response_model=list[user_schemas.UserCheck])
async def get_all_users(db: Session = Depends(get_db), admin: user.User = Depends(check_admin)):
    users = db.query(user.User).all()
    return users
