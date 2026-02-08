import mysql.connector

def get_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",          # change if needed
        password="Root@123",
        database="epc"
    )