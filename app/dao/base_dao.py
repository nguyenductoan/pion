import MySQLdb as sql

class BaseDao:
    host = 'localhost'
    user = 'root'
    password = ''
    db_name = 'lixibox'

    def __init__(self): pass

    def connect(self):
        self.db = sql.connect(host=self.host,user=self.user,db=self.db_name)
        return self.db

    def close(self):
        self.db.close()


