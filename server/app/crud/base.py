from typing import Generic, Type, TypeVar

from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.db.base_class import Base

ModelType = TypeVar('ModelType', bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class CRUDBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, model: Type[ModelType]):
        self.model = model

    def index(self, db: Session, skip: int = 0, limit: int = 100):
        return db.query(self.model).offset(skip).limit(limit).all()

    def get(self, db: Session, id: int):
        return db.query(self.model).get(id)

    def create(self, db: Session, obj_in: CreateSchemaType):
        db_obj = self.model(**obj_in.dict())
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(self, db: Session, db_obj: ModelType, obj_in: UpdateSchemaType):
        update_data = obj_in.dict(exclude_unset=True)
        for field in db_obj.dict():
            if field in update_data:
                setattr(db_obj, field, update_data[field])
        db.merge(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def remove(self, db: Session, id: int):
        obj = db.query(self.model).get(id)
        db.delete(obj)
        db.commit()
        return obj
