import sys
import pytest
import os


daos = os.path.dirname(os.path.abspath(__file__)) + "/../src/DAOs/"
models = os.path.dirname(os.path.abspath(__file__)) + "/../src/Models/"

if daos not in sys.path:
    sys.path.append(daos)

if models not in sys.path:
    sys.path.append(models)

try:
    from Client import Client
    from ClientDAO import ClientDAO
    from ClientDAOPostgres import ClientDAOPostgres
except ImportError as e:
    print(e)


def test_isInstanceEquals():
    clientDAO = ClientDAO([ClientDAOPostgres()])
    clientDAO2 = ClientDAO([ClientDAOPostgres()])
    assert clientDAO is clientDAO2


def test_save():
    clientDAO = ClientDAO(ClientDAOPostgres())
    client = Client()
    client.name = "test_clientDAO::test_save"
    client.address = "test_clientDAO::test_save"
    client.birthday = "2000-01-01"
    assert clientDAO.save(client) == True


def test_delete():
    clientDAO = ClientDAO(ClientDAOPostgres())
    client = Client()
    client.name = "test_clientDAO::test_delete"
    client.address = "test_clientDAO::test_delete"
    client.birthday = "2000-01-01"
    clientDAO.save(client)
    assert clientDAO.delete(client.id) == True


def test_delete():
    clientDAO = ClientDAO(ClientDAOPostgres())
    client = Client()
    client.name = "test_clientDAO::test_update"
    client.address = "test_clientDAO::test_update"
    client.birthday = "2000-01-01"
    clientDAO.save(client)

    client.name = "test_clientDAO::test_update2"
    client.address = "test_clientDAO::test_update2"
    client.birthday = "2000-01-02"

    assert clientDAO.update(client) == True


def test_get():
    """TODO - TEST DOESNT WORK WHEN COMPARE LIST VALUES

    """

    clientDAO = ClientDAO(ClientDAOPostgres())
    client = Client()
    client.name = "test_clientDAO::test_get"
    client.address = "test_clientDAO::test_get"
    client.birthday = "2000-01-01"
    clientDAO.save(client)

    # current test
    result = clientDAO.get(client.id)

    expected = {}
    expected[type(ClientDAOPostgres())] = []
    expected[type(ClientDAOPostgres())].append(client)

    assert expected == result

"""
if __name__ == "__main__":
    test_get()
"""

