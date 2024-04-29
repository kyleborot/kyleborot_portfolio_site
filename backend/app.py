from flask import Flask
import pyodbc


app = Flask(__name__)

#SQL config
server = '[INSERT SERVER NAME HERE]'
database = 'user_authentication' #use as db name
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
