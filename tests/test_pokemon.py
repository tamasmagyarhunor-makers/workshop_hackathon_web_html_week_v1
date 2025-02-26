from lib.pokemon import Pokemon

def test_pokemon_construcs():
    pokemon = Pokemon(1, "Pikachu", "electric")

    assert pokemon.id == 1
    assert pokemon.name == 'Pikachu'
    assert pokemon.type == 'electric'

def test_pokemon_prints_nicely():
    pokemon = Pokemon(1, "Pikachu", "electric")

    assert str(pokemon) == "Pokemon(1, Pikachu, electric)"

def test_two_pokemons_equal():
    pokemon = Pokemon(1, "Pikachu", "electric")
    pokemon_2 = Pokemon(1, "Pikachu", "electric")

    assert pokemon == pokemon_2
