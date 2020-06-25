import os
import sys
# ABC is python interface (actually is an abstract class), all interfaces have to extend it
from abc import ABC, abstractmethod
from typing import List

models = os.path.dirname(os.path.abspath(__file__)) + "/../Models/"

if models not in sys.path:
    sys.path.append(models)

try:
    #    <module>       <class>
    from Product import Product
except ImportError as e:
    print(e)
    
class ProductDAOInterface(ABC):
    """Product DAO interface
    (actually this isn't an interface at all since the methods have body, it's an abstract class)
    
    Implements:
        ABC {Abstract class} 
    
    Raises:
        NotImplementedError

    """
    @abstractmethod
    def save(self, product: Product) -> bool:
        raise NotImplementedError(f"{__class__.__name__} save Method not implemented")
    
    @abstractmethod
    def delete(self, product: Product) -> bool:
        raise NotImplementedError(
            f"{__class__.__name__} delete Method not implemented")

    @abstractmethod
    def update(self, product: Product) -> bool:
        raise NotImplementedError(
            f"{__class__.__name__} update Method not implemented")

    @abstractmethod
    def get(self, id: int) -> Product:
        raise NotImplementedError(
            f"{__class__.__name__} get Method not implemented")

    @abstractmethod
    def get(self, column: str, value) -> Product:
        raise NotImplementedError(
            f"{__class__.__name__} get Method not implemented")

    @abstractmethod
    def getAll(self) -> List[Product]:
        raise NotImplementedError(
            f"{__class__.__name__} getAll Method not implemented")
        