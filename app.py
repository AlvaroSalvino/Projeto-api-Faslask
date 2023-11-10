from flask import Flask
from flask_restful import Resource, Api
from models import Pessoas

app = Flask(__name__)
api = Api(app)


class Pessoa(Resource):
    def get(self, nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        response = {
            'nome': pessoa.nome,
            'idade': pessoa.idade,
            'id': pessoa.id
        }
        return response


api.add_resource(Pessoa, '/pessoa/<string:nome>/')

if __name__ == '__main__':
    app.run(debug=True)
