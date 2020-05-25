"""
Class for sqlite database operation
"""

import sqlite3
from sqlite3 import Error

def connect(db_file='../data/pcf.db'):
    """ create a database connection to the SQLite database
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn