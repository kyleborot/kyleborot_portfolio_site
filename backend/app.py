from flask import Flask
from routes.main_routes import main_routes
from routes.login_routes import login_routes
from config.config import conn
import secrets


app = Flask(__name__)

app.config['SECRET_KEY'] = secrets.token_hex(16)

app.register_blueprint(main_routes)
app.register_blueprint(login_routes, url_prefix='/login')

if __name__ == "__main__":
  app.run(debug=True)
