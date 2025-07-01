from fastapi import APIRouter, Depends, status, Response, HTTPException
from typing import List
import models
from schemas import showBlog, Blog, BlogUpdate,User
from database import get_db
from sqlalchemy.orm import Session
from repository import blog
from oauth2 import get_current_user

router = APIRouter(tags = ['blogs'], prefix = '/blogs')

@router.get('/', response_model = List[showBlog])
def all(db:Session = Depends(get_db), current_user:User = Depends(get_current_user)):
    return blog.get_all(db)

@router.post('/', status_code = 201)
def create_blog(request: Blog, db:Session = Depends(get_db), current_user:User = Depends(get_current_user)):
    return blog.create(request, db)

@router.get('/{id}', status_code = status.HTTP_200_OK, response_model = showBlog)
def show(id, response:Response, db:Session = Depends(get_db), current_user:User = Depends(get_current_user)):
    return blog.show(id, response, db)

@router.delete('/{id}', status_code = status.HTTP_204_NO_CONTENT)
def delete_blog(id, db:Session = Depends(get_db), current_user:User = Depends(get_current_user)):
    return blog.delete(id, db)

@router.put('/{id}', status_code = status.HTTP_202_ACCEPTED)
def update_blog(id, request: BlogUpdate, db:Session = Depends(get_db), current_user:User = Depends(get_current_user)):
    return blog.update(id, request, db)