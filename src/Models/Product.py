from dataclasses import dataclass

'''
this decorator auto generates __init__ method (constructor), so the attributes'
class are already required by the constructor
'''
@dataclass
class Product(object):
    '''
    Python doesn't have encapsulation, so the following attributes are not private
    or protected, they're all public, setters and getters are optional
    '''
    _id : int
    _name: str
    _price: float
        
    '''
    "@property" defines a getter
    "attribute.setter" defines a setter
    "attribute.deleter" defines a function to be executed when delete an attribute
    *IMPORTANT: getters come before the setters!!!
    '''
    @property
    def id_(self):
        return self._id
    
    @id_.setter
    def id_(self, id_):
        self._id = id_
        
    # deleter is automatically executed when called del <obj>.<attr>. E.g: del product.id
    @id_.deleter
    def id_(self):
        self._id = None
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name
    
    @name.deleter
    def name(self):
        self._name = None
    
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, price):
        if isinstance(price, float):
            self._price = price
        else:
            raise TypeError('Price has to be float')
        
    @price.deleter
    def price(self):
        self._price = None


    def __str__(self):
        """Way to print the object to user
        """
        return f"(id={self.id_}, name='{self.name}', price='{self.price}')"


    def __repr__(self):
        """Way to print the object to developer
        """
        return f"{__class__.__name__}(id={self.id_}, name='{self.name}', price='{self.price}')"


    def __eq__(self, other):
        return self.__repr__() == other.__repr__()
        
'''        
if __name__ == '__main__':
    product = Product(1, 'beibleide', 9.99)
    print(str(product))
    del product.name
    print(str(product))
'''