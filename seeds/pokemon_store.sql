DROP TABLE IF EXISTS pokemons;
DROP SEQUENCE IF EXISTS pokemons_id_seq;

-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS pokemons_id_seq;
CREATE TABLE pokemons (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    type VARCHAR(255)
);

-- Finally, we add any records that are needed for the tests to run
INSERT INTO pokemons (name, type) VALUES ('Pikachu', 'electric');
INSERT INTO pokemons (name, type) VALUES ('Raichu', 'electric');
INSERT INTO pokemons (name, type) VALUES ('Charmander', 'fire');
