import csv
from pokemonClass import Pokemon


def load_pokemon(csv_path):
    """Load Pokémon vectors from a CSV file.

    The CSV is expected to have a header row with a name column followed by
    numeric feature columns. Each subsequent row represents a Pokémon.
    """
    pokemons = []
    with open(csv_path, newline="") as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader, None)  # skip header if present
        for row in reader:
            if not row:
                continue
            name, *vector_values = row
            vector = [float(v) for v in vector_values]
            pokemons.append((name, Pokemon(vector)))
    return pokemons


if __name__ == "__main__":
    pokemon_list = load_pokemon("pokemon.csv")
    print(f"Loaded {len(pokemon_list)} Pokémon from CSV.")
