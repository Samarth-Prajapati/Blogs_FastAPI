from fastapi import FastAPI, Depends, status, Response
from schemas import Blog
import models
from database import engine, sessionLocal
from sqlalchemy.orm import Session
# import uvicorn

app = FastAPI()

models.Base.metadata.create_all(engine)

def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get('/')
def home():
    return {'data':'Blog List'}

# @app.get('/blog?limit=10')    
# @app.get('/blog')    
# def blog(id:int, limit = 10):
#     return {'data':id}

@app.post('/blog', status_code = 201)
def create_blog(request: Blog, db:Session = Depends(get_db)):
    new_blog = models.Blog(title = request.title, body = request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

@app.get('/blog')
def all(db:Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs

@app.get('/blog/{id}', status_code = status.HTTP_200_OK)
def show(id, response:Response, db:Session = Depends(get_db)):
    blogs = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blogs:
        response.status_code = status.HTTP_404_NOT_FOUND
    return blogs

# if __name__ == '__main__':
#     uvicorn.run(app, host = '127.0.0.1', port = 2327)