import pyodbc
import urllib
import pandas as pd
from openpyxl.utils.dataframe import dataframe_to_rows
from sqlalchemy import create_engine 
# SQL Server'dan verileri alma
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-G1HC1O3\TEST;'
                      'Database=turko;'
                      'Trusted_Connection=yes;')

# SQLAlchemy bağlantısı oluşturma
conn_str = 'mssql+pyodbc:///?odbc_connect={}'.format(
    urllib.parse.quote_plus('DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-G1HC1O3\TEST;DATABASE=turko;Trusted_Connection=yes;')
)
# cursor = conn.cursor()
# sql = "EXEC spDonemIciSatisButun @baslangic = ?, @bitis = ?,@depoInds = ?"
# cursor.execute(sql, ('2023.01.01', '2023.01.31','4'))
# sonuc = cursor.fetchall()
# print(sonuc)

engine = create_engine(conn_str)
query = "SELECT * FROM Stoklar"
df = pd.read_sql(query, engine)


writer = pd.ExcelWriter('D:\python\stoklar.xlsx')
df.to_excel(writer, index=False)
writer._save()


# C-149591316
