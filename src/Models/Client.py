from datetime import datetime

class Client(object):
    __id = 0
    __name = ""
    __address = ""
    __birthday = ""


    @property
    def id(self):
        return self.__id


    @property
    def name(self):
        return self.__name


    @property
    def address(self):
        return self.__address


    @property
    def birthday(self):
        return self.__birthday


    @id.setter
    def id(self, id):
        self.__id = id


    @name.setter
    def name(self, name):
        self.__name = name


    @address.setter
    def address(self, address):
        self.__address = address


    @birthday.setter
    def birthday(self, birthday):
        datetime.strptime(birthday, "%Y-%m-%d")
        self.__birthday = birthday

    