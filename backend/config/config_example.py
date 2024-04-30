import pyodbc

SERVER_NAME = "[INSERT SERVER CONFIG HERE]"
DATABASE_NAME = "user_authentication"
DRIVER = '{ODBC Driver 17 for SQL Server}'

conn = pyodbc.connect('DRIVER='+DRIVER+';SERVER='+SERVER_NAME+';DATABASE='+DATABASE_NAME+';Trusted_Connection=yes;')