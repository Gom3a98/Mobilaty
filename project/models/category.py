from project.config.Database import connection
from flask import jsonify


class Category:

    def __init__(self):
        self.conn = connection()
        self.cursor = self.conn.connection.cursor(dictionary=True)

    def add_category(self, params):
        val = "'{}'".format(params['cat_id'])
        self.cursor.execute("INSERT INTO mobilaty.category" +
                            " (cat_id	 , cat_name)" +
                            " VALUES (" + val + ",'" + params['cat_name'] + "')")
        self.conn.connection.commit()

    def delete_category(self, params):
        val = "'{}'".format(params['cat_id'])
        self.cursor.execute('DELETE FROM  mobilaty.category WHERE cat_id= ' + val)
        self.conn.connection.commit()
        # row = cursor.fetchone()

    def show_Allcategory(self):
        self.cursor.execute('SELECT * FROM mobilaty.category')
        row = self.cursor.fetchall()
        return row

    def update_category(self, params):
        val = "'{}'".format(params['cat_id'])
        self.cursor.execute("update mobilaty.category set cat_name = '" +
                            params['cat_name'] + "'   where cat_id = " + val)
        self.conn.connection.commit()

    def show_category(self, params):
        val = "'{}'".format(params['cat_id'])
        self.cursor.execute('SELECT * FROM mobilaty.category WHERE cat_id = ' + val + " ORDER BY RAND()")
        row = self.cursor.fetchall()
        return row

    def findByCategoryId(self, params):
        val = "'{}'".format(params['cat_id'])
        self.cursor.execute('SELECT * FROM mobilaty.category WHERE cat_id = ' + val)
        row = self.cursor.fetchall()
        return row
