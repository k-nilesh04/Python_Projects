import requests

while True:
    name = input("Enter the name of the pokemon: ").strip().lower()
    url = f"https://pokeapi.co/api/v2/pokemon/{name}"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        print(f"\n--- {data['name'].upper()} ---\n")
        print(f"Height: {data['height']}")
        print(f"Weight: {data['weight']}")
        print(f"Base Experience: {data['base_experience']}")
        print(f"Abilities: {', '.join([ability['ability']['name'] for ability in data['abilities']])}")
        print(f"Stats: {', '.join([f"{stat['stat']['name']}: {stat['base_stat']}" for stat in data['stats']])}")
        print(f"Moves: {', '.join([move['move']['name'] for move in data['moves'][:10]])}")

        types = [t['type']['name'] for t in data['types']]
        print(f"Types: {', '.join(types)}\n")
        print(f"Image URL: {data['sprites']['front_default']}\n")
        print("-" * 40 , "\n")

    else:
        print("Pokémon not found! Check your spelling.")
        break
