from pydantic import BaseModel
from typing import List


# Most fields are optional because there will be times when it will not
# be possible to get all the information. It will depend on how the pdf
# extraction is done.

class Copiavel(BaseModel):
    valor: str = ""
    copiado: bool = False

class Combustivel(BaseModel):
    potencia: Copiavel = Copiavel()
    tipo_combustivel: Copiavel = Copiavel()


class Motor(BaseModel):
    cilindradas: Copiavel = Copiavel()
    nro_cilindradas: Copiavel = Copiavel()
    combustiveis: List[Combustivel] = []


class Veiculo(BaseModel):
    desc_cat: Copiavel = Copiavel()
    renavam_desc: Copiavel = Copiavel()
    sigla: Copiavel = Copiavel()
    pacote_def_modelo: Copiavel = Copiavel()
    versao: Copiavel = Copiavel()
    ano: Copiavel = Copiavel()
    marca: Copiavel = Copiavel()
    linha: Copiavel = Copiavel()
    motor: Motor = Motor()
    carga: Copiavel = Copiavel()
    num_passag: Copiavel = Copiavel()
    num_portas: Copiavel = Copiavel()
    num_renavam: Copiavel = Copiavel()
    status: str = "PENDENTE"
    producao: Copiavel = Copiavel()
    desc_vendas: Copiavel = Copiavel()
