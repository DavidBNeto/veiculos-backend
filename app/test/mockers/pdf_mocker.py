from datetime import date
from app.api.models.pdf import PDF
from app.api.models.veiculo import Combustivel, Copiavel, Motor, Veiculo


# This function will return a Veiculo instance with mocked data.
def mock_veiculo_with_default_params() -> Veiculo:
    return Veiculo(
        desc_cat=Copiavel(valor="desc"),
        renavam_desc=Copiavel(valor="renavam"),
        sigla=Copiavel(valor="1234Test"),
        pacote_def_modelo=Copiavel(valor="pacote"),
        versao=Copiavel(valor="versao"),
        ano=Copiavel(valor="ano"),
        marca=Copiavel(valor="marca"),
        linha=Copiavel(valor="linha"),
        motor=Motor(
            cilindradas=Copiavel(valor="cilindradas"),
            nro_cilindradas=Copiavel(valor="nro_cilindradas"),
            combustiveis=[Combustivel(
                potencia=Copiavel(valor="potencia"),
                tipo_combustivel=Copiavel(valor="tipo_combustivel")
                )]
        ),
        carga=Copiavel(valor="carga"),
        num_passag=Copiavel(valor="num_passag"),
        num_portas=Copiavel(valor="num_portas"),
        num_renavam=Copiavel(valor="num_renavam")
    )

def build_pdf_with_default_params() -> PDF:
    today = date.today()
    date_string = today.strftime("%Y-%m-%d")

    return PDF(
        nome="TEST Example PDF",
        status="PENDENTE",
        ultimo_visto=date_string,
        criado=date_string,
        veiculos=[mock_veiculo_with_default_params()]
    )