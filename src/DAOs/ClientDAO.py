import os
import sys
from abc import ABC, abstractmethod

models = os.path.dirname(os.path.abspath(__file__)) + "/../Models/"

if models not in sys.path:
    sys.path.append(models)

try:
    from Client import Client
except ImportError as e:
    print(e)

'''
Interface client
'''
class ClientDAO(ABC):
    @abstractmethod
    def save(self, Client: Client) -> bool:
        pass

    @abstractmethod
    def delete(self, Client: Client) -> bool:
        pass

    @abstractmethod
    def update(self, Client: Client) -> bool:
        pass

    @abstractmethod
    def get(self, id: int) -> Client:
        pass

    @abstractmethod
    def get(self, column: str, value) -> Client:
        pass

    @abstractmethod
    def getAll(self) -> Client[]:
        pass