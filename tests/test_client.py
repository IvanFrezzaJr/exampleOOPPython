import sys
import pytest
import os
import json

models = os.path.dirname(os.path.abspath(__file__)) + "/../src/Models/"

if models not in sys.path:
    sys.path.append(models)

try:
    from Client import Client
except ImportError as e:
    print(e)


client = Client()
def test_class():
    assert isinstance(client, Client)


def test_id():
    client.id_ = 4
    assert client.id_ == 4


def test_name():
    client.name = "Ivan"
    assert client.name == "Ivan"


def test_address():
    client.address = "7 pairc na Cullean"
    assert client.address == "7 pairc na Cullean"


def test_birthday():
    client.birthday = "1988-03-25"
    assert client.birthday == "1988-03-25"


@pytest.mark.xfail(raises=ValueError)
def test_birthday_wrong():
    client.birthday = "1988-03-"


def test_repr():
    client.id_ = 1
    client.name = "Ivan"
    client.address = "7 Pairc na Cullean"
    client.birthday = "1988-03-25"

    result = repr(client)
    expected = "Client(id_=1, name='Ivan', address='7 Pairc na Cullean', birthday='1988-03-25')"
    assert result == expected
