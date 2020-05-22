import mysql.connector




class connection():
    def init(self):
       self.connection = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "",
            database = 'mobilaty'
        ) 
    def close(self):
        self.connection.close()
        