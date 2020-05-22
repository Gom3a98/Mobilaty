import mysql.connector    

class connection():
    connection = ""
    def __init__(self):
        print("Hello, Connection is Done!")
        self.connection = mysql.connector.connect(
                host = "localhost",
                user = "root",
                password = "",
                database = 'mobilaty'
            )
        
    def close(self):
        print("Hello, Connection is Terminated!")
        self.connection.close()
        