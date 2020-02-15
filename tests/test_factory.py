import sys
import pytest
import os
import psycopg2 as postgres

daos = os.path.dirname(os.path.abspath(__file__)) + "/../src/DAOs/"

if daos not in sys.path:
    sys.path.append(daos)

try:
    from Factory import Factory, DBDriver
except ImportError as e:
    print(e)


def test_instance():

    dao = Factory.connect(DBDriver.POSTGRES)
    assert isinstance(dao, postgres.extensions.connection)


def test_connection():
    dao = Factory.connect(DBDriver.POSTGRES)
    with dao.cursor() as cursor:
        cursor.execute("SELECT 1;")
        record = cursor.fetchone()
        assert record[0] == 1