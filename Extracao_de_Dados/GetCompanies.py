import yfinance as yf
from datetime import datetime
import pandas as pd



def get_companies_df():

    tickers = [
    "PETR4.SA",  # Petrobrás
    "ITUB4.SA",  # Banco Itaú
    "VALE3.SA",  # Vale
    "BPAC11.SA", # Banco BTG Pactual
    "ABEV3.SA",  # Ambev
    "BBAS3.SA",  # Banco do Brasil
    "BBDC3.SA",  # Banco Bradesco
    "WEGE3.SA",   # Weg
    "ITSA4.SA",   # Itaúsa
    "VIVT3.SA"    # Telefônica Brasil

]
    dfs = []

    '''Obter as cotações das 10 maiores empresas da B3'''
    try:
        
        for ticker in tickers:
            df_companies = yf.Ticker(ticker).history(period="1d", interval="1m")[['Close']].tail(1)
            df_companies = df_companies.rename(columns = {'Close': 'preco'})
            df_companies['ativo'] = ticker
            df_companies['moeda'] = 'BRL'
            df_companies['horario_coleta'] = datetime.now()
            df_companies = df_companies[['ativo', 'moeda', 'preco', 'horario_coleta']]
            dfs.append(df_companies)
        return pd.concat(dfs, ignore_index=True)
    
    except Exception as e:
        print(f"Erro ao obter as cotações: {e}")
        return None