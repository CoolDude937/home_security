from flask import Flask, jsonify
from flask_cors import CORS
import collections

app = Flask(__name__)

app.config.from_object(__name__)

CORS(app, resources={r"/*":{'origins':"http://localhost:8080/face-recognition"}})

# hello world route
@app.route('/', methods = ['GET'])
def greetings():
    return ("Hello, world!")

if __name__ == "__main__":
    app.run(debug=True)