from model.base import Base

from sqlalchemy import create_engine, exists
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types import Integer, Numeric, String, Date

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    address = Column(String)

    def __init__(self, email, first_name, last_name, address):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.address = address

