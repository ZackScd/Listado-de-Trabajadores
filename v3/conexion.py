import mysql.connector

class BaseDatos:
    def __init__(self):
        self.conn = mysql.connector.connect(
        host = "localhost",
        user = "root",
        port = "3306",
        database = "ListaTrabajadores")

        self.cursor = self.conn.cursor()