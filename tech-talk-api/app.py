#!flask/bin/python
from flask import Flask, jsonify, abort

app = Flask(__name__)

articles = [
    {
        'id': 1,
        'hat': u'hands on',
        'title': u'Buy groceries',
        'summary': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
    },
    {
        'id': 2,
        'hat': u'hands on',
        'title': u'Learn Python',
        'summary': u'Need to find a good Python tutorial on the web', 
    }
]

@app.route('/techtalk/api/v1.0/articles', methods=['GET'])
def get_articles():
    return jsonify({'articles': articles})

if __name__ == '__main__':
    app.run(debug=True)