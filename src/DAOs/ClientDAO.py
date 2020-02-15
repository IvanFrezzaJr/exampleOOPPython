from ClientDAOInterface import ClientDAOInterface
from Client import Client
from typing import List

from ClientDAOPostgres import ClientDAOPostgres


class ClientDAO(object):
    """TODO DEPENDECE INJECTIONS OF CLIENT DAO POSTGRES, ETC
    
    Arguments:
        object {[type]} -- [description]
    """

    __clientDAOs = None
    _instance = None

    '''
    def __init__(self, clientDAOs: List[ClientDAOInterface]):
        if isinstance(clientDAOs, list):
            self.__clientDAOs = clientDAOs
        else:
            self.__clientDAOs = [clientDAOs]
    '''

    def __new__(self, clientDAOs: List[ClientDAOInterface]):
        """Singleton
        """
        if not self._instance:
            if isinstance(clientDAOs, list):
                self.__clientDAOs = clientDAOs
            else:
                self.__clientDAOs = [clientDAOs]

            self._instance = super(ClientDAO, self).__new__(self)

        return self._instance


    def save(self, client: Client) -> None:
        result = []
        for dao in self.__clientDAOs:
            try:
                result.append(dao.save(client))
                if not all(result):
                    return False

            except Exception as e:
                print(e)
                return False

        return True


    def update(self, client: Client) -> None:
        result = []
        for dao in self.__clientDAOs:
            try:
                result.append(dao.update(client))
                if not all(result):
                    return False

            except Exception as e:
                print(e)
                return False

        return True


    def delete(self, client: Client) -> None:
        result = []
        for dao in self.__clientDAOs:
            try:
                result.append(dao.delete(client))
                if not all(result):
                    return False

            except Exception as e:
                print(e)
                return False
        return True


    def get(self, id: int) -> Client:

        clients = {}

        for dao in self.__clientDAOs:
            try:
                clients[dao.__class__] = []
                clients[dao.__class__].append(dao.get(id))
            except Exception as e:
                print(e)
                return False

        return clients


    def getAll(self):
        """TODO - IMPLEMENT METHOD NEXT WEAK
        """
        pass


if __name__ == "__main__":
    clientDAO = ClientDAO(ClientDAOPostgres())
    client = Client()
    client.name = "Joao Pinto Rola"
    client.address = "La pra la de la"
    client.birthday = "2000-01-01"
    print(clientDAO.get(131))
