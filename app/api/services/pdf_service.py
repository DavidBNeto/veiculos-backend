from http.client import HTTPException
from typing import List
from app.api.models.pdf import PDF
from app.api.repositories.pdf_repository import PDFRepository


class PDFService:
    def __init__(self, repository: PDFRepository):
        self._repository = repository

    def get_all(self) -> List[PDF]:
        return self._repository.get_all()

    def get_by_nome(self, nome: str) -> PDF:
        try:
            return self._repository.get_by_nome(nome)
        except Exception:
            raise HTTPException(
                status_code=404, detail="PDF nao encontrado por nome.")
        
    def create(self, pdf_data: PDF) -> PDF:
        result = self._repository.create(pdf_data)
        return self._repository.find_by_id(result.inserted_id)

    def update(self, nome: str, pdf_data: PDF) -> PDF:
        result = self._repository.update(nome, pdf_data)
        if result.modified_count == 0:
            raise HTTPException(
                status_code=400, detail="Nenhum dado encontrado ou modificado.")
        return self._repository.get_by_nome(nome)

    def delete(self, nome: str) -> str:
        result = self._repository.delete(nome)
        if result.deleted_count == 0:
            raise HTTPException(
                status_code=400, detail="Dado nao encontrado para deletar.")
        return nome