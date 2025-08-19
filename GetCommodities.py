import yfinance as yf
from datetime import datetime
import pandas as pd



def get_commodities_df():

    tickers = ['GC=F', 'SI=F', 'CL=F']  # Ouro, Prata, Petróleo WTI
    dfs = []

    '''Obter as cotações de commodities'''
    try:
        
        for ticker in tickers:
            df_commodities = yf.Ticker(ticker).history(period="1d", interval="1m")[['Close']].tail(1)
            df_commodities = df_commodities.rename(columns = {'Close': 'preco'})
            df_commodities['ativo'] = ticker
            df_commodities['moeda'] = 'USD'
            df_commodities['data_coleta'] = datetime.now()
            df_commodities = df_commodities[['ativo', 'preco', 'moeda', 'data_coleta']]
            dfs.append(df_commodities)
        return pd.concat(dfs, ignore_index=True)
    
    except Exception as e:
        print(f"Erro ao obter as commodities: {e}")
        return None
    

print(get_commodities_df())