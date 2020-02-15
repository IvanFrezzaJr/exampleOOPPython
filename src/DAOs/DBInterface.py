import os
import sys
from abc import ABC, abstractmethod
from typing import List
#from __future__ import notations # para funcionar tipagem no python 2.7


class DBInterface(ABC):
    """Database interface
    
    Arguments:
        ABC {Abstract class} 
    
    Raises:
        NotImplementedError

    """
    @abstractmethod
    # object: type
    def save(self, sql: str) -> int:
        raise NotImplementedError("save Method not implemented")

    @abstractmethod
    def delete(self, sql: str) -> bool:
        raise NotImplementedError("delete Method not implemented")

    @abstractmethod
    def update(self, sql: str) -> bool:
        raise NotImplementedError("update Method not implemented")

    @abstractmethod
    def get(self, id: int) -> tuple:
        raise NotImplementedError("get Method not implemented")

    @abstractmethod
    def getAll(self) -> List[tuple]:
        raise NotImplementedError("getAll Method not implemented")