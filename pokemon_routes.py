from lib.database_connection import get_flask_database_connection
from lib.pokemon_repository import PokemonRepository
from lib.pokemon import Pokemon
from flask import request, render_template, redirect, url_for

def apply_pokemon_routes(app):
    @app.route('/pokemons', methods=['GET'])
    def get_pokemons():
        connection = get_flask_database_connection(app)
        repository = PokemonRepository(connection)

        pokemons = repository.all()
        return render_template('pokemons/index.html', pokemons=pokemons)