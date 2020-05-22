from project.config.Database import connection
from flask import jsonify


class Store:

    def __init__(self):
        self.conn = connection()
        self.cursor = self.conn.connection.cursor()

    def add_store(self, params):
        self.cursor.execute("INSERT INTO mobilaty.store" +
                            " (store_name , store_descreption ,store_img , address)" +
                            " VALUES ('" + params['store_name'] + "','" + params['store_descreption'] +
                            "','" + params['store_img'] + "','" + params['address'] + "')")
        self.conn.connection.commit()

    def delete_store(self, params):
        self.cursor.execute('DELETE FROM  mobilaty.store WHERE store_id= ' + params['store_id'])
        self.conn.connection.commit()
        # row = cursor.fetchone()

    def show_AllStore(self):
        self.cursor.execute('SELECT * FROM mobilaty.store')
        row = self.cursor.fetchall()
        return row

    def update_store(self, params):
        self.cursor.execute(
            "update mobilaty.store set store_name= '" + params['store_name'] + "' store_descreption = '" +
            params['store_descreption'] + "'and store_img= '" + params['store_img'] + "' and address= '" +
            params['address'] + "'  where store_id = " + params['store_id'])
        self.conn.connection.commit()

    def show_store(self, params):
        self.cursor.execute('SELECT * FROM mobilaty.store WHERE store_id = ' + params['store_id'] + " ORDER BY RAND()")
        row = self.cursor.fetchall()
        return row
