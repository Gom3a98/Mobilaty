from project.config.Database import connection 
from flask import  jsonify

class Comment:

    def __init__(self):
        self.conn = connection()
        self.cursor = self.conn.connection.cursor()
    def add_comment(self,params):

        self.cursor.execute("INSERT INTO mobilaty.comment" +
            " (post_id, comment_body,user_id)" +
            " VALUES ('" + params['post_id'] + "','" + params['comment_body'] +
            "','" + params['user_id'] + "')")
        self.conn.connection.commit()
  
    def show_comment(self,params):
        self.cursor.execute('SELECT * FROM mobilaty.comment WHERE post_id = '
                            + params['post_id']+" ORDER BY RAND()")
        row = self.cursor.fetchall()
        return row

    def show_AllComment(self):
        self.cursor.execute('SELECT * FROM mobilaty.comment')
        row = self.cursor.fetchall()
        return row

    def update_comment(self,params):
        self.cursor.execute("update mobilaty.comment set comment_body = '" +
            params['comment_body'] + "' where comment_id = " + params['comment_id'])
        self.conn.connection.commit()
        #row = cursor.fetchone()

    def delete_comment(self,params):
        self.cursor.execute('DELETE FROM  mobilaty.comment WHERE comment_id = '+params['comment_id'])
        self.conn.connection.commit()
        #row = cursor.fetchone()