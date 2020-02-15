from DBInterface import DBInterface
from Factory import Factory
from Factory import DBDriver
import os
import sys
from typing import List, overload

if os.getenv("DEBUG") == 1:
    reload(Factory)


"""TODO WE MIGHT WANT TO USE POOL FACTORY TO RECYCLE OBJECTS

"""

class DBPostgres(DBInterface):

    Factory.POSTGRES = 2
    _conn = Factory.connect(DBDriver.POSTGRES)
    _instance = None
    _records = None

    def __new__(self):
        """Singleton
        """
        if not self._instance:
            self._instance = super(DBPostgres, self).__new__(self)
        return self._instance

    def execute(self, sql: str)-> int:
        with self._conn.cursor() as cursor:
            cursor.execute(sql)

            try:
                self._records = cursor.fetchall()

            except Exception as e:
                print(f"{e} \n Use RETURNING at the end of the query to get deleted values. E.g.: <query> RETURNING id;")
                self._records = None

            return cursor.rowcount


    def get_records(self):
        return self._records

    def save(self, sql: str) -> int:
        with self._conn.cursor() as cursor:
            cursor.execute(sql)
            return cursor.fetchone()[0]
