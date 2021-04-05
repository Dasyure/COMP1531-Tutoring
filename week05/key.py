import requests
from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample tags = 'div', 'img'
@app.route('/getcount', methods=['GET'])
def addname():
    content = requests.get("https://www.unsw.edu.au/").text
    tag = request.args.get('tag')
    count = content.count(f'<{tag}')
    return jsonify({
        'tag_count': count,
    })

if __name__ == '__main__':
    app.run()

