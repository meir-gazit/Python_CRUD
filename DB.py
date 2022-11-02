from time import time
from psycopg2.extras import RealDictCursor
import psycopg2

class DB():
    def __init__(self):
        while True:

            try:
                conn = psycopg2.connect(host='localhost', database='pyCRUD', user='postgres', password='sa', cursor_factory=RealDictCursor)
                print("connected to DB")
                break
            except Exception as error:
                print("fail to connect to DB: ", error)
                time.sleep(2)
        return conn