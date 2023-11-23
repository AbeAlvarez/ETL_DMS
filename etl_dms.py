#%%
import sqlalchemy
from sqlalchemy import create_engine
import pyodbc
import pandas as pd
pyodbc.drivers()


# %%
user = 'ssmsdb'
password = '123456'
server = '1C3CR3AM-001'
database = 'bi_db'

engine = create_engine(f'mssql+pyodbc://{user}:{password}@{server}/{database}?driver=ODBC+Driver+17+for+SQL+Server')
conn = engine.connect()

    
# %%
query = 'SELECT * FROM dbo.customers;'
df = pd.read_sql(query, conn)
df.head()

# %%
path = 'data\data_dms_20180101.csv'
df_raw_data = pd.read_csv(path)
df_raw_data.head()

# %%
query_ship_modes = 'SELECT * FROM dbo.shipModes'
df_ship_modes = pd.read_sql(query_ship_modes, conn)
df_ship_modes.head()
#%%
