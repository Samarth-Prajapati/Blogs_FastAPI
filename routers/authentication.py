from datetime import timedelta 
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from schemas import Login
from database import get_db
from sqlalchemy.orm import Session
import models
from hashing import Hash
from JWT_Token import create_access_token

router = APIRouter(tags = ['authentication'], prefix = '/authenticate')

@router.post('/login')
def login(request:OAuth2PasswordRequestForm = Depends(), db:Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == request.username).first()
    if not user:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f'Username Not Found')
    if not Hash.verify(user.password, request.password):
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f'Wrong Password')
    access_token = create_access_token(data = {'sub':user.email})
    return {'access_token':access_token, 'token_type':'bearer'}