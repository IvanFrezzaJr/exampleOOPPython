class Product(object):
    __id = 0
    __name = ''
    __price = ''
    
    @property
    def id(self):
        return self.__id
    
    @property
    def name(self):
        return self.__name
    
    @property
    def price(self):
        return self.__price
    
    @id.setter
    def id(self, id):
        self.__id = id
        
    @name.setter
    def name(self, name):
        self.__name = name
        
    @price.setter
    def price(self, price):
        self.__price = price