import sys
import pytest
import os
import psycopg2 as postgres


daos = os.path.dirname(os.path.abspath(__file__)) + "/../src/DAOs/"
models = os.path.dirname(os.path.abspath(__file__)) + "/../src/Models/"

if daos not in sys.path:
    sys.path.append(daos)

try:
    from ClientDAOPostgres import ClientDAOPostgres
    from Client import Client
except ImportError as e:
    print(e)


clientDAOPostgres = ClientDAOPostgres()
def test_instance():
    assert isinstance(clientDAOPostgres, ClientDAOPostgres)


def test_save():
    client = Client()
    client.name = "test - save client"
    client.address = "test - save client"
    client.birthday = "2000-01-01"

    client_Result = clientDAOPostgres.save(client)

    assert client_Result == True


def test_delete():
    client = Client()
    client.name = "test - delete client"
    client.address = "test - delete client"
    client.birthday = "2000-01-01"
    clientDAOPostgres.save(client)
    assert clientDAOPostgres.delete(client.id) == True


def test_get():
    client = Client()
    client.name = "test - get client"
    client.address = "test - get client"
    client.birthday = "2000-01-01"
    clientDAOPostgres.save(client)
    assert clientDAOPostgres.get(client.id) == client


def test_getall():

    clients_expected = []
    clients_result = []

    clientDAOPostgres.execute("TRUNCATE TABLE client CASCADE;")

    _instance = None

    for c in range(1, 5):
        client = Client()
        client.name = f"test {c} - get client"
        client.address = f"test {c} - get client"
        client.birthday = f"2000-01-0{c}"

        if clientDAOPostgres.save(client):
            clients_expected.append(client)

    for gen_client in clientDAOPostgres.getAll():
        clients_result.append(gen_client)

    assert clients_result == clients_expected


def test_update():
    """TODO YOU MIGHT NEED TO MAKE THE test_save TO RETURN THE CLIENT OBJECT
        TO MAKE SURE THAT OBJECT BEING UPDATED EXISTS
    """
    """TODO ADD COLUMN TIMESTAMP INTO DATABASE
        ALTER TABLE client ADD COLUMN created_at SET DEFAULT now();
    """
    client = Client()
    client.name = "Test - update client"
    client.address = "Test - update client"
    client.birthday = "2000-01-01"
    clientDAOPostgres.save(client)

    client.name = "Test - update client"
    client.address = "Test - update client"
    client.birthday = "1980-01-01"
    assert clientDAOPostgres.update(client) == True


def test_isInstanceEquals():
    clientDAOpg = ClientDAOPostgres()
    clientDAOpg2 = ClientDAOPostgres()
    assert clientDAOpg is clientDAOpg2
