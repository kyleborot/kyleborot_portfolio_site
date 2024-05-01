from flask import Blueprint
from config.config import conn

main_routes = Blueprint('main', __name__)

@main_routes.route("/")
def hello():
  return "Hello World!"

@main_routes.route("/test")
def test():
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM LoginSchema.Users") #SQL Connection Test
    data = cursor.fetchall()
    cursor.close()
    return str(data)