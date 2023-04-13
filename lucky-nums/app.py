from flask import Flask, render_template, request, jsonify
from flask_debugtoolbar import DebugToolbarExtension
import random
import requests
import json


app = Flask(__name__)

app.config["SECRET_KEY"] = "oh-so-secret"

debug = DebugToolbarExtension(app)



@app.route("/")
def homepage():
    """Show homepage."""

    return render_template("index.html")

@app.route('/api/get-lucky-num', methods=['POST'])
def get_lucky_num():
    """get responses and if validated calls api  """

    response = {}

    birth_year = request.json['birth_year']
    name = request.json['name']
    email = request.json['email']
    color = request.json['color']
    response['errors'] = validate_inputs([birth_year, name, email, color])

    if response['errors'] == {}:
        response = call_api(birth_year)
        
    return jsonify(response)

def validate_inputs(inputs):
    """validates each specific input"""
    errors = {}
    if inputs[0] == "" or int(inputs[0]) < 1900 or int(inputs[0]) > 2000 :
        errors['birth_year'] = ["Invalid Input, year must be between 1900 and 2000"]
    if inputs[1] == "":
        errors['name'] = ["Input required"]
    if inputs[2] == "":
        errors['email'] =  ["Input required"]
    if inputs[3] not in ['Red', 'Blue', 'Green', 'Orange']:
        errors['color'] =  ["Invalid value, must be one of: red, green, orange, blue."]
    return errors

def call_api(birth_year):
    """calls on api for random number and facts"""
    response = {}
    num = random.randint(0,100)
    response1 = requests.get(f'http://numbersapi.com/{num}/trivia')
    response2 = requests.get(f'http://numbersapi.com/{birth_year}/year')
    response["num"] = {"fact":f'{response1.text}', "num":num}
    response["year"] = {"fact":f'{response2.text}', "year":birth_year}

    return response