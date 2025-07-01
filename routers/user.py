from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from schemas import showUser, User
from database import get_db
import models
from hashing import Hash
from repository import user

router = APIRouter(tags = ['users'], prefix = '/user')

@router.post('/', response_model = showUser)
def create_user(request: User, db:Session = Depends(get_db)):
    return user.create(request, db)

@router.get('/{id}', response_model = showUser)
def show_user(id, db:Session = Depends(get_db)):
    return user.show(id, db)