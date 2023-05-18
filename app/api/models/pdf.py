from pydantic import BaseModel
from typing import List

from app.api.models.veiculo import Veiculo


class PDF(BaseModel):
    nome: str
    status: str = "PENDENTE"
    ultimo_visto: str
    criado: str
    veiculos: List[Veiculo]
