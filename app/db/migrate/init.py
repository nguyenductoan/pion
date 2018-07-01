from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.types import Integer, Numeric, String, Date
from sqlalchemy.schema import Table, Column, ForeignKey, MetaData
from sqlalchemy.ext.declarative import declarative_base
import pdb

engine = create_engine('mysql+mysqldb://root@localhost/pion')

if not database_exists(engine.url):
    create_database(engine.url)

metadata = MetaData(engine)
if not engine.dialect.has_table(engine, 'users'):
    Table('users', metadata,
            Column('id', Integer, primary_key=True, nullable=False),
            Column('email', String(16), primary_key=True, nullable=False),
            Column('last_name', String(16)),
            Column('last_name', String(16)),
            Column('created_at', Date)
           )
metadata.create_all()

