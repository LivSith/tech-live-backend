#!flask/bin/python
from flask import Flask, jsonify, abort, \
    make_response, request

app = Flask(__name__)

articles = [
    {
        'id': 1,
        'hat': u'hands on',
        'title': u'Criamos uma API Python usando Flask',
        'summary': u'O que vcs acharam do Flask', 
    },
    {
        'id': 2,
        'hat': u'Heads Off',
        'title': u'Aqui está a Integração',
        'summary': u'Artigos da nossa API... Lembra o que a Livia Mostrou?', 
    },
    {
        'id': 3,
        'hat': u'hands on',
        'title': u'O Que é Mais Dificil em ser DEV?',
        'summary': u'Viver é dificil!', 
    },
    {
        'id': 4,
        'hat': u'Heads Off',
        'title': u'Então é Isso?',
        'summary': u'Quanto mais aprendemos, percebemos que não sabemos nada!', 
    },
    {
        'id': 5,
        'hat': u'Heads Off',
        'title': u'Sua Vez',
        'summary': u'Aprender e compartilhar - Assim como a verdade, de graça recebemos de graça compartilhamos!',
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