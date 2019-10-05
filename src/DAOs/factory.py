from postgres import *
from abc import ABC

'''
Final Class
'''
class Factory(ABC):
    POSTGRES = 1
    __postgresDAO = None

    @classmethod
    def connect(cls, dao):
        if dao == cls.POSTGRES:
            if not cls.__postgresDAO:
                cls.__postgresDAO = Postgres("postgres://example@localhost/exampleooppython")
            return cls.__postgresDAO


