from mongodb_connect import MongoDBConnection

class InventoryDB(MongoDBConnection):
    def __init__(self,db_name):
        super().__init__()
        self.collection = self.database_getir()['inventory']

    def insert_inventory_data(self,data):
        self.collection.insert_many(data)