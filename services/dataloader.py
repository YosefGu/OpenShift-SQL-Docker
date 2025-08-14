import mysql.connector
import os


class DataLoader():

    def __init__(self):
        self.conn = mysql.connector.connect(
            host=os.getenv("MYSQL_HOST"),
            user=os.getenv("MYSQL_USER"),
            password=os.getenv("MYSQL_PASSWORD"),
            database=os.getenv("MYSQL_DATABASE")
        )


    def get_data(self):
        cursor = self.conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM users;")
        return cursor.fetchall()
    
    def add_data(self, user):
        cursor = self.conn.cursor(dictionary=True)
        try:
            cursor.execute(f"INSERT INTO users (id, first_name, last_name) VALUES (${user.id}, ${user.first_name}, ${user.last_name});")
        except Exception as e:
            print("Error::", e)
            return e