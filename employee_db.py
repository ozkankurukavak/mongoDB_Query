from mongodb_connect import MongoDBConnection

class EmployeeDB(MongoDBConnection):
    def __init__(self, db_name):
        super().__init__()
        self.collection = self.database_getir(db_name)["calisan_bilgileri"]

    def calisan_ekleme(self, data):
        self.collection.insert_one(data)
    def coklu_calisan_ekleme(self, data):
        self.collection.insert_many(data)

    def calisanlari_gosterme(self):
        return self.collection.find({}) # Bütün çalışanları getirir.
    
    def isimlerine_gore_calisan_bulma(self, ilk_isim):
        return self.collection.find({'firstname':ilk_isim})
    
    def kalitesine_gore_calisan_bulma(self, kalite_derecesi):
        return self.collection.find({"$in":kalite_derecesi})

    def yasina_ve_kalitesine_gore_calisan_bulma(self,kalite_derecesi, yas):
        return self.collection.find({'qualification':kalite_derecesi, 'age':{"$lt":yas}})
    
    def sorgulara_gore_calisan_gosterme(self, sorgu):
        return self.collection.find({"$or":sorgu})