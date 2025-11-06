from fastapi import APIRouter,Depends,HTTPException,status

from sqlalchemy.orm import Session
from sqlalchemy import func
from .. import models,schema
from ..database import get_db
from ..auth.auth import verify_api_key


router = APIRouter(prefix="/books",tags=["Books"])

@router.post("/",response_model=schema.BookRead,status_code=status.HTTP_201_CREATED)
def create_book(book:schema.BookCreate,db:Session=Depends(get_db),_:None=Depends(verify_api_key)):
    try:
        new_book = models.Book(title=book.title,description=book.description)
        db.add(new_book)
        db.commit()
        db.refresh(new_book)
        return new_book
    
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400,detail=f"Error: {str(e)}")


@router.get("/",response_model=list[schema.BookRead])
def get_books(skip:int=0,limit:int=10,title:str|None=None,db:Session=Depends(get_db),_:None=Depends(verify_api_key)):
    query = db.query(models.Book)
    if title:
        query = query.filter(models.Book.title.contains(title))
    return query.offset(skip).limit(limit).all()


@router.get("/{book_id}",response_model=schema.BookRead)
def get_book(book_id:int,db:Session=Depends(get_db),_:None=Depends(verify_api_key)):
    book = db.query(models.Book).filter(models.Book.id==book_id).first()
    if not book:
        raise HTTPException(status_code=404,detail=f"Book with {book_id} ID not found")
    return book


@router.put("/{book_id}",response_model=schema.BookRead)
def update_book(book_id:int,updated:schema.BookUpdate,db:Session=Depends(get_db),_:None=Depends(verify_api_key)):
    book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404,detail=f"Book with {book_id} ID not found")
    
    for field,value in updated.dict(exclude_unset=True).items():
        setattr(book,field,value)
    
    db.commit()
    db.refresh(book)
    return book


@router.delete("/{book_id}",status_code=status.HTTP_200_OK)
def delete_book(book_id:int,db:Session=Depends(get_db),_:None=Depends(verify_api_key)):
    book = db.query(models.Book).filter(models.Book.id==book_id).first()
    if not book:
        raise HTTPException(status_code=404,detail=f"Book with {book_id} ID not found")
    db.delete(book)
    db.commit()
    return {"message":f"Book with {book.id} ID eleted"}    



# Demonstrate Transaction Handling
@router.post("/create-and-update", summary="Create and Update in a single api")
def create_and_update(db: Session = Depends(get_db),_:None=Depends(verify_api_key)):

    try:
        # Start transaction
        new_book = models.Book(title="Ikigai", description="Created in transaction")
        db.add(new_book)

        # Commit not yet called 
        db.flush()  # Flush so new_book.id is generated

        #Update in same transaction
        new_book.title = "Think grow and riches"

        # Commit both steps together
        db.commit()
        db.refresh(new_book)

        return {"message": "Transaction successful", "book": {
            "id": new_book.id,
            "title": new_book.title,
            "created_at": str(new_book.created_at)
        }}

    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"Transaction failed: {str(e)}")