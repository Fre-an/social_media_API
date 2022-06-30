from typing import List
from fastapi import status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from .. import models, schemas, oauth2
from ..database import get_db

router = APIRouter(
    tags=["Comment"]
)

@router.post("/comment", status_code=status.HTTP_201_CREATED)
def create_comment(comment: schemas.Comment, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    post_query = db.query(models.Post).filter(models.Post.id == comment.post_id)

    if not post_query.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id {id} was not found")

    new_comment = models.Comment(user_id = current_user.id, content = comment.content, post_id = comment.post_id)
    db.add(new_comment)
    db.commit()
    return {"message": "Comment successfully added"}

@router.get("/posts/{id}/comments", response_model=List[schemas.CommentOut])
def get_comments(id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    comments = db.query(models.Comment).filter(models.Comment.post_id == id).all()

    if not comments:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No comments found")

    return comments