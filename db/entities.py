from sqlalchemy.orm import relationship, backref, joinedload
from sqlalchemy import Column, DateTime, String, Integer, Float, ForeignKey, func, UniqueConstraint

from db.base import Base, inverse_relationship, create_tables 


class BillItem(Base):
    __tablename__ = 'bill_items'
    id = Column(Integer, primary_key=True)
    
    description = Column(String, nullable=False, unique=True)
    amount = Column(Float, nullable=False)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())


if __name__ != '__main__':
    create_tables()