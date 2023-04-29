import pyodbc   <------ import library
import urllib
import pandas as pd
from openpyxl.utils.dataframe import dataframe_to_rows
from sqlalchemy import create_engine 
# SQL Server'dan verileri alma
conn = pyodbc.connect('Driver={SQL Server};'  
                      'Server=SERVER\TEST;' <-------------------------- SQL SERVER NAME 
                      'Database=turko;'  <---------------------------- SQL DATABASE NAME  
                      'Trusted_Connection=yes;') 

# SQLAlchemy bağlantısı oluşturma
conn_str = 'mssql+pyodbc:///?odbc_connect={}'.format(
    urllib.parse.quote_plus('DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-G1HC1O3\TEST;DATABASE=turko;Trusted_Connection=yes;') 
)


engine = create_engine(conn_str)
query = "SELECT * FROM Stoklar"
df = pd.read_sql(query, engine)


writer = pd.ExcelWriter('D:\python\stoklar.xlsx')  <------ OUTPUT FİLES
df.to_excel(writer, index=False)
writer._save()
