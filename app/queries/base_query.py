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

    def all(self, limit=1000):
        session = session_factory()
        query = session.query(self.model)
        query = query.limit(limit)
        session.close()
        return query.all()

    def find(self, id):
        session = session_factory()
        query = session.query(self.model)
        query = query.filter_by(id=id)
        session.close()
        return query.all()

    def filter_by(self, conditions):
        session = session_factory()
        query = session.query(self.model)
        for key, value in conditions.items():
            query = query.filter(getattr(self.model, key) == value)
        session.close()
        return query.all()

    def plain_sql(self, statement, params):
        session = session_factory()
        # Ex: statement: 'SELECT * FROM orders WHERE orders.id < :val'
        # params: { 'val': 50 }
        query = session.execute(statement, params)
        session.close()
        return query.fetchall()

