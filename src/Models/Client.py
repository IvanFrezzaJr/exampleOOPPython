from datetime import datetime
import json

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

    # deleter is automatically executed when called del <obj>.<attr>. E.g: del client.name
    @id.deleter
    def id(self):
        self.__id = None


    @name.deleter
    def name(self):
        self.__name = None


    @address.deleter
    def address(self):
        self.__address = None


    @birthday.deleter
    def birthday(self):
        self.__birthday = None


    def __str__(self):
        """Way to print the object to user
        """
        return f"(id={self.id}, name='{self.name}', address='{self.address}', birthday='{self.birthday}')"


    def __repr__(self):
        """Way to print the object to developer
        """
        return f"{__class__.__name__}(id={self.id}, name='{self.name}', address='{self.address}', birthday='{self.birthday}')"


    def __eq__(self, other):
        return self.__repr__() == other.__repr__()


if __name__ == "__main__":
    client = Client()
    print(client)
