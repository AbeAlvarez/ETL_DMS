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
query = "SELECT TOP 1000 customerid, genderid FROM dbo.customers;"
df = pd.read_sql(query, conn)
df.head()