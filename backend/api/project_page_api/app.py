from flask import Flask, jsonify
from flask_cors import CORS
from projects import projects

app = Flask(__name__)
CORS(app) 


"""
project info interface:
id - int
name - string
description - string
isDemo - bool
photoURL - string
createdDate - string
createdLocation - string
techUsed - string
"""

@app.route('/projects', methods=['GET'])
def get_projects():
    return jsonify(projects)

if __name__ == '__main__':
    app.run(debug=True)
