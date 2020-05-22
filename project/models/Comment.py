from project.config.Database import connection 
from flask import  jsonify

class Comment:

    def __init__(self):
        self.conn = connection()
        self.cursor = self.conn
    def add_comment(self,params):

        self.cursor.execute("INSERT INTO mobilaty.comment" +
            " (post_id, comment_body,user_id)" +
            " VALUES ('" + params['post_id'] + "','" + params['comment_body'] +
            "','" + params['user_id'] + "')")
  
    def show_comment(self,params):
        self.cursor.execute('SELECT * FROM mobilaty.comment WHERE post_id = '
                            + params['post_id']+" ORDER BY RAND()")
        r = [dict((self.cursor.description[i][0], value)
              for i, value in enumerate(row)) for row in self.cursor.fetchall()]
        return jsonify({'myCollection' : r})
    def update_comment(self,params):
        self.cursor.execute("update mobilaty.comment set comment_body = '" +
            params['comment_body'] + "' where comment_id = " + params['comment_id'])
        #row = cursor.fetchone()

    def delete_comment(self,params):
        self.cursor = self.conn
        self.cursor.execute('DELETE FROM  mobilaty.comment WHERE comment_id = ?', params['comment_id'])
        #row = cursor.fetchone()