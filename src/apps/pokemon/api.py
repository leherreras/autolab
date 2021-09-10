import json
import logging

from flask import jsonify, request
from flask_classy import FlaskView, route

from .controller import pokemons


class PokemonView(FlaskView):

    @route('/', methods=['GET', 'POST'])
    def pokemons(self):
        try:
            query = json.loads(request.args.get('query', default='{}'))
            page = request.args.get('page', default=1, type=int)
            per_page = int(request.args.get('per_page', default=10, type=int))
            return jsonify(pokemons(page, per_page, query))
        except AttributeError as e:
            logging.info(str(e))
            return jsonify(error=str(e)), 404
