# Write a simple flask server names.py that does the following:
#   Has a route that can take a name and a date of birth (as a unix timestamp)
#   Has a route that will produce all names/ages of people who've been entered previously

from datetime import datetime
from flask import Flask, jsonify, request

app = Flask(__name__)

names = []

def date_to_age(timestamp):
    dt = datetime.fromtimestamp(timestamp)
    now = datetime.now()
    diff = now - dt
    return diff.days // 365


@app.route('/addname', methods=['POST'])
def addname():
    data = request.get_json()
    names.append({
        'name': data['name'],
        'age': date_to_age(int(data['dob']))
    })
    print(data)
    return {}

@app.route('/getnames', methods=['GET'])
def getnames():
    return jsonify(names)

if __name__ == '__main__':
    app.run()