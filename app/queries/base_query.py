from sqlalchemy import create_engine, exists
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from model import *

engine = create_engine('mysql+mysqldb://root@localhost/lixibox')
# use session_factory() to get a new Session
SessionFactory = sessionmaker(bind=engine)

def session_factory():
    return SessionFactory()

class BaseQuery():

    def all(self, class_name, limit=1000):
        session = session_factory()
        orders_query = session.query(class_name).limit(limit)
        session.close()
        return orders_query.all()

    def find(self, class_name, id):
        session = session_factory()
        orders_query = session.query(class_name).filter_by(id=id)
        session.close()
        return orders_query.all()

