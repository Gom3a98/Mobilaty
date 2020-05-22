from project.config.Database import connection
from flask import jsonify, session
import bcrypt


class User:

    def __init__(self):
        self.conn = connection()
        self.cursor = self.conn.connection.cursor()

    def LogInGet(self, params):
        if 'username' in session:
            session.pop('username', None)
            session.pop('password', None)
        session['username'] = params['username']
        session['password'] = params['password']
        return "LogIN Done."

    def LogInPost(self, params):
        val = "'{}'".format(params['username'])
        # val = params['username']
        self.cursor.execute('SELECT * FROM mobilaty.user WHERE name =' + val + "and password = "+params['password'])
        row = self.cursor.fetchall()
        if len(row) <= 0:
            return "There is no user with this info."
        return "LogIN Done."

    def SignupGet(self, params):
        if 'username' in session:
            session.pop('username', None)
            session.pop('password', None)
        self.createuser(params)
        return "Signup Done."

    def SignupPost(self, params):
        if 'username' in session:
            session.pop('username', None)
            session.pop('password', None)
        self.createuser(params)
        return "Signup Done."

    def getAllUsers(self):
        self.cursor.execute('SELECT * FROM mobilaty.user')
        row = self.cursor.fetchall()
        return row

    def getUserById(self, params):
        self.cursor.execute('SELECT * FROM mobilaty.user WHERE id = ' + params['id'])
        row = self.cursor.fetchall()
        return row

    def createuser(self, params):
        self.cursor.execute("INSERT INTO mobilaty.user" +
                            " (name, email,password,age,address,type)" +
                            " VALUES ('" + params['name'] + "','" + params['email'] + "','" + params['password']
                            + "','" + params['age'] + "','" + params['address'] + "','" + params['type'] + "')")

        self.conn.connection.commit()

    def removeuser(self, params):
        self.cursor.execute('DELETE FROM  mobilaty.user WHERE id = ' + params['id'])
        self.conn.connection.commit()

    def finduserByUserName(self, params):
        val = "'{}'".format(params['username'])
        self.cursor.execute('SELECT * FROM  mobilaty.user where name =' + val)
        row = self.cursor.fetchall()
        return row

    def hashfun(self, password):

        hashed = bcrypt.hashpw(password, bcrypt.gensalt())
        return hashed

    def compare(userPassword, hashPassword):
        if bcrypt.checkpw(userPassword, hashPassword):
            return True
        else:
            return False
