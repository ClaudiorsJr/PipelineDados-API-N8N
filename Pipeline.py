import pandas as pd
import time
from sqlalchemy import create_engine
from Extracao_de_Dados.GetBitcoin import get_bitcoin_df
from Extracao_de_Dados.GetCommodities import get_commodities_df
from Extracao_de_Dados.GetCompanies import get_companies_df
from dotenv import load_dotenv
import os

# carrega as variaveis de abiente do arquivo .env
load_dotenv()

# Configura a conexao com o banco de dados postgresql
db_user = os.getenv('user')
db_password = os.getenv('password')
db_host = os.getenv('host')
db_port = os.getenv('port')
db_name = os.getenv('dbname')

#conexão com sqlalchemy
db_url = f'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}'
engine = create_engine(db_url)

if __name__=="__main__":
    while True:
        # Obtenção dos dados
        df_bitcoin = get_bitcoin_df()
        df_commodities = get_commodities_df()
        df_companies = get_companies_df()

        # Concatenação dos dataframes
        df = pd.concat([df_bitcoin, df_commodities, df_companies], ignore_index=True)

        # Inserção dos dados no banco de dados
        df.to_sql('cotacoes',con=engine, if_exists='append', index=False)
        print("Dados inseridos com sucesso!")

        # Espera por 60 segundos antes de repetir o processo
        time.sleep(60)