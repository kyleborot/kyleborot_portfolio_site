from flask import Flask
import pyodbc
from config import SERVER_NAME, DATABASE_NAME


app = Flask(__name__)

#SQL config
server = SERVER_NAME
database = DATABASE_NAME
driver = '{ODBC Driver 17 for SQL Server}'

conn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';DATABASE='+database+';Trusted_Connection=yes;')

@app.route("/")
def hello():
  return "Hello World!"

@app.route("/test")
def test():
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM LoginSchema.Users") #SQL Connection Test
    data = cursor.fetchall()
    cursor.close()
    return str(data)

if __name__ == "__main__":
  app.run(debug=True)
