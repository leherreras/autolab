from flask import jsonify
from flask_classy import FlaskView

from .controller import pokemons


class PokemonView(FlaskView):
    def index(self):
        response = pokemons()
        return jsonify(response)
