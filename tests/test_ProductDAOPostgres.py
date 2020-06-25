import sys
import pytest
import os
import psycopg2 as postgres

daos = os.path.dirname(os.path.abspath(__file__)) + "/../src/DAOs/"

if daos not in sys.path:
    sys.path.append(daos)

try:
    from ProductDAOPostgres import ProductDAOPostgres
    from Product import Product
except ImportError as e:
    print(e)

'''
Usage: pytest tests/test_ProductDAOPostgres.py -s -vv
'''    

productDAOPostgres = ProductDAOPostgres()
def test_instance():
    assert isinstance(productDAOPostgres, ProductDAOPostgres)
    
def test_save():
    product = Product(None, 'bleibleide', 1.99)
    assert productDAOPostgres.save(product) == True
    
def test_delete():
    product = Product(None, 'bleibleide', 1.99)
    productDAOPostgres.save(product)
    assert productDAOPostgres.delete(product.id_) == True
    
def test_get():
    product = Product(None, 'bleibleide', 1.99)
    productDAOPostgres.save(product)
    assert productDAOPostgres.get(product.id_) == product