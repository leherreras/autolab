from apps.pokemon.api import PokemonView


def create_routes(app):
    """
    Register all EndPoints eg.
    App.register(app)
    :param app: Flask app create in main file project
    """
    PokemonView.register(app)
