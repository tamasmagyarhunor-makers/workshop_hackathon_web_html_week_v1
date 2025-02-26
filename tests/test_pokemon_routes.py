from playwright.sync_api import Page, expect

def test_get_pokemons(db_connection, page, test_web_address):
    db_connection.seed("seeds/pokemon_store.sql")

    page.goto(f"http://{test_web_address}/pokemons")

    list_items = page.locator("li")

    expect(list_items).to_have_text([
        "Pikachu is the type: electric",
        "Raichu is the type: electric",
        "Charmander is the type: fire"
    ])

def xtest_get_pokemon(db_connection, page, test_web_address):
    db_connection.seed("seeds/pokemon_store.sql")

    page.goto(f"http://{test_web_address}/pokemons")

    page.click("text=Raichu is the type: electric")

    title_element = page.locator(".t-title")
    expect(title_element).to_have_text("Name: Raichu")

    author_element = page.locator(".t-type")
    expect(author_element).to_have_text("Type: electric")

def xtest_create_pokemon(db_connection, page, test_web_address):
    db_connection.seed("seeds/pokemon_store.sql")
    page.goto(f"http://{test_web_address}/pokemons")

    page.click("text=Add a new pokemon")

    page.fill("input[name='name']", "Charizard")

    page.fill("input[name='type']", "fire")

    page.click("text=Create Pokemon")

    title_element = page.locator(".t-name")
    expect(title_element).to_have_text("Name: Charizard")

    author_element = page.locator(".t-type")
    expect(author_element).to_have_text("Type: fire")