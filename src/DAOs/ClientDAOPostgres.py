from ClientDAOInterface import ClientDAOInterface
from DBPostgres import DBPostgres
from Factory import Factory
from Factory import DBDriver
import os
import sys
from typing import List, overload, Generator

if os.getenv("DEBUG") == 1:
    reload(Factory)

models = os.path.dirname(os.path.abspath(__file__)) + "/../src/Models/"

if models not in sys.path:
    sys.path.append(models)

try:
    from Client import Client
except ImportError as e:
    print(e)

"""TODO WE MIGHT WANT TO USE POOL FACTORY TO RECYCLE OBJECTS

"""


class ClientDAOPostgres(DBPostgres, ClientDAOInterface):
    """BE CAREFULL ABOUT THE INHERITAGE ORDER. PYTHON GET METHODS IN THAT ORDER:
        E.G.: 
            - DBPostgres.save()
            - ClientDAOInterface.save()
    
    Extends:
        DBPostgres {[type]} -- [description]
        ClientDAOInterface {[type]} -- [description]
    
    Returns:
        [type] -- [description]
    
    Yields:
        [type] -- [description]
    """

    def __init__(self):
        super(ClientDAOPostgres, self).__init__()


    def __new__(self):
        """Singleton
        """
        if not self._instance:
            self._instance = super(ClientDAOPostgres, self).__new__(self)
        return self._instance

    def save(self, client: Client) -> bool:

        sql = f"INSERT INTO client(name, address, birthday) VALUES ('{client.name}', '{client.address}', '{client.birthday}') RETURNING id;"


        """CALLS DBPostgres.save() BECAUSE IS THE FIRST INHERITED CLASS
        """
        if super().execute(sql):
            # first [0] gets record and second [0] gets id.

            client.id_ = super().get_records()[0][0]

            return True
        return False



    def delete(self, id_: int) -> bool:
        """TODO WE BETTER PASS THE WHOLE OBJECT TO BE ABLE TO RECYCLE
        """
        sql = f"DELETE FROM client WHERE id = {id_} RETURNING id;"

        if super().execute(sql):
            return True
        return False


    def update(self, client: Client) -> bool:
        sql = f"""
            UPDATE client SET  
                name = '{client.name}',           
                address = '{client.address}',        
                birthday = '{client.birthday}'        
                WHERE id = {client.id_};
        """

        if super().execute(sql):
            return True
        return False


    def get(self, id_: int) -> Client:
        sql = f"SELECT * FROM client WHERE id = {id_};"

        if super().execute(sql):
            record = super().get_records()[0]
            if record:
                client = Client()
                client.id_ = record[0]
                client.name = record[1]
                client.address = record[2]
                client.birthday = str(record[3])
                return client

        return None


    def getAll(self) -> List[Client]:
        """Get all

        Get all records from client table
        
        Returns:
            List[Client] -- list of objects clients
        
        Yields:
            List[Client] -- generator 
        """
        self._conn.autocommit = False

        with self._conn.cursor(name="client", scrollable=True) as cursor:

            cursor.execute("select * from client;")

            index = 0

            while True:

                try:
                    cursor.scroll(index, mode='absolute')

                except (ProgramingError, IndexError) as e:
                    print(e)
                    print("generator")

                record = cursor.fetchone()

                if record:
                    client = Client()
                    client.id_ = record[0]
                    client.name = record[1]
                    client.address = record[2]
                    client.birthday = str(record[3])
                    yield client

                else:
                    break

                index = index + 1

        
