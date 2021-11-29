import sqlite3


sql_create = '''
CREATE TABLE IF NOT EXISTS orders
(id INTEGER PRIMARY KEY,
item text,
customer text,
seller text,
price text);
'''

sql_fetch = 'SELECT * FROM orders'

sql_insert = 'INSERT INTO orders VALUES (null, ?, ?, ?, ?)'

sql_remove = 'DELETE FROM orders WHERE id=?'

sql_delete_all = 'DROP table orders'

sql_update = 'UPDATE orders SET item = ?, customer = ?, seller = ?, price = ? WHERE id=?'

class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.curr = self.conn.cursor()
        self.curr.execute(sql_create)
        self.conn.commit()

    def fetch(self):
        self.curr.execute(sql_fetch)
        return self.curr.fetchall()

    def insert(self, item, customer, seller, price):
        self.curr.execute(sql_insert, (item,customer,seller,price))
        self.conn.commit()

    def remove(self, id):
        self.curr.execute(sql_remove, (id, ))

    def drop_table(self):
        self.curr.execute(sql_delete_all)

    def update(self, id, item, customer, seller, price):
        self.curr.execute(sql_update, (item,customer,seller,price, id))
        self.conn.commit()


    def __del__(self):
        self.conn.close()

db = Database("store.db")

db.insert('laptop', 'Zhambul Nuray', 'Oppo', '500')
db.insert('phone', 'Temirbay Margulan', 'Samsung', '550')
db.insert('mouse', 'Zhambul Mukhammedali', 'Apple', '999')
db.insert('charger', 'Sarsenov Zhambul', 'Samsung', '20')
db.insert('monitor', 'Sarsenova Gulmira', 'Dell', '180')
db.insert('phone', 'Shildebayeva Saida', 'Apple', '999')
db.insert('hdd', 'Sovet Temirlan', 'WD', '150')


# db.drop_table()
