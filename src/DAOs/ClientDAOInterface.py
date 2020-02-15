import os
import sys
from abc import ABC, abstractmethod
from typing import List
#from __future__ import notations # para funcionar tipagem no python 2.7

models = os.path.dirname(os.path.abspath(__file__)) + "/../Models/"

if models not in sys.path:
    sys.path.append(models)

try:
    from Client import Client
except ImportError as e:
    print(e)



class ClientDAOInterface(ABC):
    """Client DAO interface
    
    Arguments:
        ABC {Abstract class} 
    
    Raises:
        NotImplementedError

    """
    @abstractmethod
    # object: type
    def save(self, client: Client) -> bool:
        raise NotImplementedError(f"{__class__.__name__} save Method not implemented")

    @abstractmethod
    def delete(self, client: Client) -> bool:
        raise NotImplementedError(
            f"{__class__.__name__} delete Method not implemented")

    @abstractmethod
    def update(self, client: Client) -> bool:
        raise NotImplementedError(
            f"{__class__.__name__} update Method not implemented")

    @abstractmethod
    def get(self, id: int) -> Client:
        raise NotImplementedError(
            f"{__class__.__name__} get Method not implemented")

    @abstractmethod
    def get(self, column: str, value) -> Client:
        raise NotImplementedError(
            f"{__class__.__name__} get Method not implemented")

    @abstractmethod
    def getAll(self) -> List[Client]:
        raise NotImplementedError(
            f"{__class__.__name__} getAll Method not implemented")
