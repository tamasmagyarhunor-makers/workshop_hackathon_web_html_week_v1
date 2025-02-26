from lib.pokemon import Pokemon

class PokemonRepository():
    def __init__(self, db_connection):
        self._db_connection = db_connection

    def all(self):
        rows = self._db_connection.execute('SELECT * from pokemons')
        pokemons = []
        for row in rows:
            item = Pokemon(row["id"], row["name"], row["type"])
            pokemons.append(item)
        return pokemons
    
    def create(self, pokemon):
        rows = self._db_connection.execute(
            "INSERT INTO pokemons (name, type) VALUES(%s, %s) returning id", 
            [
                pokemon.name, 
                pokemon.type
            ]
        )
        row = rows[0]
        pokemon.id = row["id"]
        return pokemon
    
    def find(self, pokemon_id):
        rows = self._db_connection.execute(
            "SELECT * FROM pokemons WHERE id = %s",
            [
                pokemon_id
            ]
        )

        pokemon = Pokemon(rows[0]['id'], rows[0]['name'], rows[0]['type'])

        return pokemon