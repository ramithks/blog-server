from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from blog.repository import user
from blog import schemas, database


router = APIRouter(
    prefix='/user',
    tags=['Users']
)
get_db = database.get_db

@router.post('/',response_model=schemas.ShowUser)
def create_user(request:schemas.User,db: Session = Depends(get_db)):
    return user.create_user(request,db)

@router.get('/{id}',response_model=schemas.ShowUser)
def get_user(id:int,db: Session = Depends(get_db)):
    return user.get_user(id,db)

