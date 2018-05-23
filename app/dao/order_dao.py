from dao.base_dao import BaseDao

class OrderDao(BaseDao):

    def __init__(self):
        super

    def fetchall(self):
        db = self.connect()
        cur = db.cursor()
        cur.execute('SELECT * FROM orders WHERE id<50')
        data = cur.fetchall()
        self.close()
        return data

