import sys
import os
import pytest

models = os.path.dirname(os.path.abspath(__file__)) + '/../src/Models/'

if models not in sys.path:
    sys.path.append(models)

try:
    from Product import Product
except ImportError as e:
    print(e)

product = Product(1, 'beibleide', 9.99)

def test_class():
    assert isinstance(product, Product)

def test_id():
    product.id_ = 5
    assert product.id_ == 5

def test_name():
    product.name = 'Jhon'
    assert product.name == 'Jhon'

def test_price():
    product.price = 1.99
    assert product.price == 1.99
    
def test_wrong_price():
    with pytest.raises(TypeError):
        product.price = '9.99'