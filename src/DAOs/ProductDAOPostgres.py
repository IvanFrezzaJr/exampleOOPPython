from ProductDAOInterface import ProductDAOInterface
from DBPostgres import DBPostgres
from Factory import Factory
from Factory import DBDriver
import os
import sys
from typing import List, overload, Generator

if os.getenv("DEBUG") == 1:
    reload(Factory)  # regenerate the .pyc file (clean cache)

models = os.path.dirname(os.path.abspath(__file__)) + "/../src/Models/"

if models not in sys.path:
    sys.path.append(models)

try:
    from Product import Product
except ImportError as e:
    print(e)
    
class ProductDAOPostgres(DBPostgres, ProductDAOInterface):
    """BE CAREFULL ABOUT THE INHERITAGE ORDER. PYTHON GET METHODS IN THAT ORDER:
        E.G.: 
            - DBPostgres.save()
            - ClientDAOInterface.save()
    
    Extends:
        DBPostgres {[type]} -- [description]
        ProductDAOInterface {[type]} -- [description]
    
    Returns:
        [type] -- [description]
    
    Yields:
        [type] -- [description]
    """
    
    def save(self, product: Product) -> bool:
        sql = f"INSERT INTO product (name, price) VALUES('{product.name}', {product.price}) RETURNING id;"
        #CALLS DBPostgres.save() BECAUSE IS THE FIRST INHERITED CLASS
        if super().execute(sql):
            # first [0] gets record and second [0] gets id.
            product.id_ = super().get_records()[0][0]
            return True
        return False
    
    def update(self, product: Product) -> bool:
        pass
    
    def get(self, id_: int) -> Product:
        sql = f"SELECT * FROM product WHERE id = {id_};"
        if super().execute(sql):
            record = super().get_records()[0]
            if record:
                product = Product(
                    record[0],
                    record[1],
                    float(record[2])
                )
                return product
        return None
    
    def delete(self, id_: int) -> bool:
        # it's a good practice finishing the sql with ';' (it tells to finish the query)
        sql = f"DELETE FROM product WHERE id = {id_};"
        if super().execute(sql):
            return True
        return False
    
    def getAll(self) -> List[Product]:
        pass
    