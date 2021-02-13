#!flask/bin/python
from flask import Flask, jsonify, abort, \
    make_response, request

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


@app.route('/techtalk/api/v1.0/articles/<int:article_id>', methods=['GET'])
def get_article(article_id):
    article = [article for article in articles if article['id'] == article_id]
    if len(article) == 0:
        abort(404)
    return jsonify({'article': article[0]})


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.route('/techtalk/api/v1.0/articles', methods=['POST'])
def create_article():
    if not request.json or not 'title' in request.json:
        abort(400)
    article = {
        'id': articles[-1]['id'] + 1,
        'hat': request.json['hat'],
        'title': request.json['title'],
        'summary': request.json.get('summary', "")
    }
    articles.append(article)
    return jsonify({'article': article}), 201


if __name__ == '__main__':
    app.run(debug=True)