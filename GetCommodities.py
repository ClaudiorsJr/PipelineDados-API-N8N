import yfinance as yf
from datetime import datetime



def get_commodities():

    '''Obter as cotações de commodities'''
    try:
        # Ouro
        df_commodities = yf.Ticker("GC=F").history(period="1d", interval="1m")[['Close']].tail(1)
        df_commodities = df_commodities.rename(columns = {'Close': 'preco'})
        df_commodities['ativo'] = 'GC=F'
        df_commodities['moeda'] = 'USD'
        df_commodities['data_coleta'] = datetime.now()
        df_commodities = df_commodities[['ativo', 'preco', 'moeda', 'data_coleta']]

        return df_commodities
    
    except Exception as e:
        print(f"Erro ao obter as commodities: {e}")
        return None

commodities_data = get_commodities()

print(commodities_data)