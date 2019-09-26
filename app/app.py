import io
import json

from flask import escape, request, jsonify, Flask

from .spellcheck import Spellchecker

app = Flask(__name__)

corrector = Spellchecker()

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'


# http http://localhost:5000/history/1/333
@app.route('/<input_term>')
def correct(input_term):
    return jsonify(corrector.get_correction(input_term))
