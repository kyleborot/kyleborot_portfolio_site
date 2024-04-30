from flask import Flask
from routes.main_routes import main_routes
from routes.login_routes import login_routes
from config.config import conn


app = Flask(__name__)

app.register_blueprint(main_routes)
app.register_blueprint(login_routes)

if __name__ == "__main__":
  app.run(debug=True)
