import requests
import pandas as pd
from datetime import datetime

def coletar_precos_bitcoin():

    """Coleta o preço atual do Bitcoin em dólares americanos (USD) da API Coinbase."""

    # URL para obter o preço atual do Bitcoin
    url = 'https://api.coinbase.com/v2/prices/spot'

    # Parâmetros da requisição
    response = requests.get(url)

    # Obter os dados da resposta
    data = response.json()

    preco = float(data['data']['amount'])
    ativo = data['data']['base']
    moeda = data['data']['currency']
    horario_coleta = datetime.now()

    # Criar um DataFrame com os dados coletados
    df = pd.DataFrame({
        'ativo': [ativo],
        'moeda': [moeda],
        'preco': [preco],
        'horario_coleta': [horario_coleta]
    })

    return df



