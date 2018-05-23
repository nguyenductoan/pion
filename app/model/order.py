from model.base import Base

from sqlalchemy import create_engine, exists
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types import Integer, Numeric, String, Date

class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True)
    number = Column(String)
    user_id = Column(Integer)
    full_address = Column(String)
    total_price = Column(Integer)

    def __init__(self, number, user_id, full_address, total_price):
        self.number = number
        self.user_id = user_id
        self.full_address = full_address
        self.total_price = total_price

