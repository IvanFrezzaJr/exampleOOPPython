import psycopg2 as postgres
from psycopg2 import ProgrammingError
from abc import ABC
import sys
import os
from enum import Enum


class DBDriver(Enum):
    """Database constants
    
    The way to declare constants in Python
    """
    POSTGRES = 1
    MYSQL = 2


class Factory(ABC):
    """Final Class - Factory to return connect object.
    
    Arguments:
        ABC -- Abstract class
    
    Returns:
        [Factory] -- Factory object
    """
    __postgresDAO = None

    @classmethod
    def connect(cls, dao):
        """Return connection
        
        Arguments:
            dao {Enum} -- Database driver constant
        
        Returns:
            any -- connection with a datasource
        """
        if dao == DBDriver.POSTGRES:
            if not cls.__postgresDAO:
                if os.environ["PRODUCTION"] == 1:
                    cls.__postgresDAO = postgres.connect("host=localhost port=5432 dbname=exampleooppython user=example")
                else:
                    cls.__postgresDAO = postgres.connect("host=localhost port=5432 dbname=exampleooppython_test user=example")

                """psycopg2 to use transaction by default. Its necessary use autocommit.
                """
                cls.__postgresDAO.autocommit = True

            return cls.__postgresDAO
