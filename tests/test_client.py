import sys
import pytest
import os 

models = os.path.dirname(os.path.abspath(__file__)) + "/../src/Models/"

if models not in sys.path:
    sys.path.append(models)

try:
    from Client import Client
except ImportErawrror as e:
    print(e)


client = Client()


def test_class():
    assert isinstance(client, Client)


def test_id():
    client.id = 4
    assert client.id == 4


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
