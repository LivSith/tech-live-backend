#!flask/bin/python
from flask import Flask, jsonify, abort, \
    make_response, request

app = Flask(__name__)

articles = [
    {
        'id': 1,
        'hat': u'hands on',
        'title': u'Criando um projeto full stack com HTML, CSS e API Python',
        'summary': u'Montes, lacus, laoreet commodo egestas amet eget laoreet. Amet et', 
    },
    {
        'id': 2,
        'hat': u'Heads Off',
        'title': u'Live',
        'summary': u'lorem lorem lorem lorem', 
    }
]

@app.route('/techtalk/api/v1.0/articles', methods=['GET'])
def get_articles():
    return jsonify({'articles': articles})


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == '__main__':
    app.run(debug=True)