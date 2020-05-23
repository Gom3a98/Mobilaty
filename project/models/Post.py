from project.config.Database import connection
from flask import jsonify


class Post:

    def __init__(self):
        self.conn = connection()
        self.cursor = self.conn.connection.cursor(dictionary=True)

    def add_post(self, params):
        self.cursor.execute("INSERT INTO mobilaty.post" +
                            " (post_description , post_img ,store_id)" +
                            " VALUES ('" + params['post_description'] + "','" + params['post_img'] +
                            "','" + params['store_id'] + "')")
        self.conn.connection.commit()

    def delete_post(self, params):
        self.cursor.execute('DELETE FROM  mobilaty.post WHERE post_id= ' + params['post_id'])
        self.conn.connection.commit()
        # row = cursor.fetchone()

    def show_AllPost(self):
        self.cursor.execute('SELECT * FROM mobilaty.post')
        row = self.cursor.fetchall()
        return row

    def update_post(self, params):
        self.cursor.execute("update mobilaty.post set post_description = '" +
                            params['post_description'] + "'and post_img= '" +
                            params['post_img'] + "'   where post_id = " + params['post_id'])
        self.conn.connection.commit()

    def show_post(self, params):
        self.cursor.execute('SELECT * FROM mobilaty.post WHERE post_id = ' + params['post_id'] + " ORDER BY RAND()")
        row = self.cursor.fetchall()
        return row

    def findByStoreId(self, params):
        self.cursor.execute('SELECT * FROM mobilaty.post WHERE store_id = ' + params['store_id'])
        row = self.cursor.fetchall()
        return row
