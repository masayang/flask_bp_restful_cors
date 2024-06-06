from flask_restful import Resource


class HolaAmigos(Resource):
    def get(self):
        return {'hola': 'amigos'}
