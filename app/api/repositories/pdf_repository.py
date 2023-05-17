from bson import ObjectId
from pymongo.database import Database
from pymongo.results import UpdateResult, DeleteResult, InsertOneResult

from app.api.models.pdf import PDF

VEICULO_COLLECTION = "PDFS"

class PDFRepository:
    def __init__(self, database: Database):
        self._collection = database[VEICULO_COLLECTION]

    def get_all(self) -> list[PDF]:
        pdfs = []
        pdfs_dict = list(self._collection.find())
        for pdf in pdfs_dict:
            pdfs.append(PDF.parse_obj(pdf))
        return pdfs
    
    def get_by_nome(self, nome: str) -> PDF:
        pdf_dict = self._collection.find_one({"nome": nome})
        return PDF.parse_obj(pdf_dict)
    
    def create(self, pdf_data: PDF) -> InsertOneResult:
        # On create we need to convert car_data to dict and then insert it into the database.
        # Ex: db.insert_one(car_data.dict())
        return self._collection.insert_one(pdf_data.dict())
    
    def update(self, nome: str, pdf_data: PDF) -> UpdateResult:
        return self._collection.update_one({"nome": nome}, {"$set": pdf_data.dict()})
    
    def delete(self, nome: str) -> DeleteResult:
        return self._collection.delete_one({"nome": nome})

    def find_by_id(self, id: ObjectId):
        return PDF.parse_obj(self._collection.find_one({"_id": id}))