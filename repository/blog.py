import models
from sqlalchemy.orm import Session
from schemas import Blog, BlogUpdate
from fastapi import HTTPException, status, Response

def get_all(db:Session):
    blogs = db.query(models.Blog).all()
    return blogs

def create(request:Blog, db:Session):
    new_blog = models.Blog(title = request.title, body = request.body, user_id = request.user_id)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def delete(id:int, db:Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f'{id} - id not found.')
    blog.delete(synchronize_session = False)
    db.commit()
    return 'Deleted Successfully'

def update(id:int, request:BlogUpdate, db:Session):
    try:
        blog = db.query(models.Blog).filter(models.Blog.id == id)
        if not blog.first():
            raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f'{id} - id not found.')
        blog.update({
        "title": request.title,
        "body": request.body
    })
    except(Exception):
        return Exception
    db.commit()
    return 'updated'

def show(id:int, response:Response, db:Session):
    blogs = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blogs:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f'Blog with id - {id} is not available')
    return blogs