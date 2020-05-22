import mysql.connector    

class connection():
    connection = ""
    def __init__(self):
        self.connection = mysql.connector.connect(
                host = "localhost",
                user = "root",
                password = "",
                database = 'mobilaty'
            )
        print("Hello, Connection is Done!")
        
    def close(self):
        self.connection.close()
        print("Hello, Connection is Terminated!")
        