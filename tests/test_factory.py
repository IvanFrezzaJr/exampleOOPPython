import sys
import pytest
import os 
from postgres import *

daos = os.path.dirname(os.path.abspath(__file__)) + "/../src/DAOs/"

if daos not in sys.path:
    sys.path.append(daos)

try:
    from factory import Factory
except ImportError as e:
    print(e)


def test_instance():
    dao = Factory.connect(Factory.POSTGRES)
    assert isinstance(dao, Postgres)


def test_connection():
    dao = Factory.connect(Factory.POSTGRES)
    assert dao.one("SELECT 1;") == 1