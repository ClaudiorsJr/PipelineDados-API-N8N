
--- Tabela bronze de cotações de ativos financeiros
--- Dados coletados das APIs (coinbase e yfinance)

CREATE TABLE IF NOT EXISTS PUBLIC.COTACOES (
  ID              BIGSERIAL PRIMARY KEY,
  ATIVO           VARCHAR(10) NOT NULL,
  PRECO           NUMERIC(15, 6) NOT NULL,
  MOEDA           CHAR(3) NOT NULL,
  HORARIO_COLETA  TIMESTAMP NOT NULL,
  DATA_CRIACAO    TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
)

--- Tabela bronze de Clientes

CREATE TABLE IF NOT EXISTS PUBLIC.BRONZE_CUSTOMERS (
  BRONZE_CUSTOMER_ID     BIGSERIAL PRIMARY KEY, -- PK da camada bronze
  CUSTOMER_ID            TEXT NOT NULL UNIQUE, -- ID de origem do cliente
  CUSTOMER_NAME          VARCHAR(200) NOT NULL,
  DOCUMENTO              VARCHAR(32),
  SEGMENTO               VARCHAR(64),
  PAIS                   VARCHAR(64),
  ESTADO                 VARCHAR(16),
  CIDADE                 VARCHAR(100),
  DATA_CRIACAO           TIMESTAMP NOT NULL
)

--- Tabela bronze de Vendas de BITCOIN (sem preço unitário)

CREATE TABLE IF NOT EXISTS PUBLIC.BRONZE_SALES_BTC_EXCEL (
  BRONZE_SALES_BTC_ID    BIGSERIAL PRIMARY KEY, -- PK append only
  TRANSACTION_ID         TEXT NOT NULL UNIQUE, -- ID de origem da venda
  DATA_HORA              TIMESTAMP NOT NULL, -- Data e hora da venda
  ATIVO                  VARCHAR(16) NOT NULL, -- Ativo vendido (BTC)
  QUANTIDADE             NUMERIC(18, 6) NOT NULL CHECK(QUANTIDADE>0), -- Quantidade de BTC vendida
  TIPO_OPERACAO          VARCHAR(16) NOT NULL CHECK(TIPO_OPERACAO IN ('COMPRA', 'VENDA')),
  MOEDA                  VARCHAR(10) NOT NULL,
  CLIENTE_ID             TEXT NOT NULL, -- refere-se ao CUSTOMER_ID da tabela de clientes
  CANAL                  VARCHAR(32),
  MERCADO                VARCHAR(8),
  ARQUIVO_ORIGEM         VARCHAR(256),
  IMPORTADO_EM           TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
)


--- Tabela bronze de Vendas de Commodities e ações (sem preço unitário)
CREATE TABLE IF NOT EXISTS bronze_sales_commodities_sql (
  BRONZE_SALES_COMM_ACOES_ID BIGSERIAL PRIMARY KEY, -- PK append-only
  TRANSACTION_ID             TEXT NOT NULL,         -- ID da origem transacional
  DATA_HORA                  TIMESTAMPTZ NOT NULL,
  COMMODITY_ACAO_CODE        VARCHAR(20) NOT NULL,  -- GOLD, OIL, COFFEE, SILVER...
  QUANTIDADE                 NUMERIC(18,6) NOT NULL CHECK (QUANTIDADE > 0),
  TIPO_OPERACAO              VARCHAR(10) NOT NULL CHECK (TIPO_OPERACAO IN ('COMPRA','VENDA')),
  UNIDADE                    VARCHAR(16) NOT NULL,  -- kg, bbl, oz...
  MOEDA                      VARCHAR(10) NOT NULL,
  CLIENTE_ID                 TEXT,                  -- referencia ao customer_id da origem
  CANAL                      VARCHAR(32),
  MERCADO                    VARCHAR(8),
  ARQUIVO_ORIGEM             VARCHAR(256),
  IMPORTADO_EM               TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);
