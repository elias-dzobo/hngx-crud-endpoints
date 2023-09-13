from models import schemas, models 
from sqlalchemy.orm import Session 
from fastapi import Depends, HTTPException, status, APIRouter, Response
from db.database import get_db


router = APIRouter() 


@router.get('/')
def get_users(db: Session = Depends(get_db), limit: int = 10, page: int = 1, search: str = ''):
    skip = (page - 1) * limit 

    users = db.query(models.User).filter(
        models.User.name.contains(search)
    ).limit(limit).offset(skip).all()

    return {'status': 'success', 'results': len(users), 'users':users}


@router.get('/{name}')
def get_user_by_name(name: str, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.name == name).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"No user with this name: {name} found")
    return {"status": "success", "user": user}

@router.patch('/{name}')
def update_user_by_name(name: str, payload: schemas.UserBaseSchema, db: Session = Depends(get_db)):
    user_query = db.query(models.User).filter(models.User.name == name).first()
    db_user = user_query.first()
    if not db_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'No user with this name: {name} found')

    update_user = payload.dict(exclude_unset=True) 
    user_query.filter(models.User.name == name).update(update_user, synchronize_session=False) 

    db.commit()
    db.refresh(db_user)

    return {'Status':'success', 'user':db_user} 



@router.post('/', status_code=status.HTTP_201_CREATED)
def create_user(payload: schemas.UserBaseSchema, db: Session = Depends(get_db)):
    new_user = models.User(**payload.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {'Status':'success', 'user': new_user}


@router.patch('/{userID}')
def update_user(userID: str, payload: schemas.UserBaseSchema, db: Session = Depends(get_db)):
    user_query = db.query(models.User).filter(
        models.User.id == userID
    )
    db_user = user_query.first()

    if not db_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'No user with this id: {userID} found')
    
    update_user = payload.dict(exclude_unset=True) 
    user_query.filter(models.User.id == userID).update(update_user, synchronize_session=False) 

    db.commit()
    db.refresh(db_user)

    return {'Status':'success', 'user':db_user} 


@router.get('/{userID}')
def get_user(userID: str, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == userID).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"No user with this id: {userID} found")
    return {"status": "success", "user": user}


@router.delete('/{userID}')
def delete_user(userID: str, db: Session = Depends(get_db)):
    user_query = db.query(models.User).filter(models.User.id == userID)
    user = user_query.first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'No user with this id: {userID} found')
    user_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.delete('/{name}')
def delete_user_by_name(name: str, db: Session = Depends(get_db)):
    user_query = db.query(models.User).filter(models.User.name == name)
    user = user_query.first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'No user with this name: {name} found')
    user_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
