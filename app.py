from flask import Flask, Blueprint
from flask_restful import Resource, Api
from resources.hello_world.hello_world import HelloWorld
from resources.hola_amigos.hola_amigos import HolaAmigos


app = Flask(__name__)
api_bp = Blueprint('api', __name__)
api = Api(api_bp)

api.add_resource(HelloWorld, '/hello_world')
api.add_resource(HolaAmigos, '/hola_amigos')
app.register_blueprint(api_bp)

if __name__ == '__main__':
    app.run(debug=True, port=5555)