from enum import Enum
from pydantic import BaseModel
from typing import List
from app.api.models.veiculo import Veiculo


# Status enum.
class Status(str, Enum):
    PENDENTE = "PENDENTE"
    EM_ANALISE = "EM_ANALISE"
    APROVADO = "APROVADO"
    REPROVADO = "REPROVADO"


# PDF class is used to store the information of a pdf.
class PDF(BaseModel):
    nome: str
    status: Status = Status.PENDENTE
    ultimo_visto: str
    criado: str
    veiculos: List[Veiculo]
