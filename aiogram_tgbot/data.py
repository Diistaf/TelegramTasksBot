import sqlite3
import random
from sqlite3 import Error


def connection_with_db(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
    except Error as e:
        print(f"Error:{e}")

    return connection

