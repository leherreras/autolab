import unittest

from app import app, db
from utils.install import install


class PokemonTestCase(unittest.TestCase):
    def setUp(self):
        """Define test variables and initialize app."""
        self.app = app
        self.client = self.app.test_client()

        # Crea un contexto de aplicación
        with self.app.app_context():
            # Crea las tablas de la base de datos
            db.create_all()
            install()

    def tearDown(self):
        """teardown all initialized variables."""
        with self.app.app_context():
            # Delete all tables in dbs
            db.session.remove()
            db.drop_all()

    def test_get_pokemons(self):
        res = self.client.get(
            '/pokemon/?query={"filter":{"name":"Venusaur","legendary":true}}&page=1&per_page=3',
            headers={"X-API-KEY": "123456"}
        )
        self.assertEqual(200, res.status_code)
        self.assertEqual({'data': [], 'next': None, 'prev': None, 'total': 0}, res.json)

    def test_unauthorized_access_pokemon(self):
        res = self.client.get('/pokemon/')
        self.assertEqual(401, res.status_code)
        self.assertEqual("Unauthorized", res.json["name"])


if __name__ == '__main__':
    unittest.main()
