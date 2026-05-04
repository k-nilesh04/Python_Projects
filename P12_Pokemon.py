import requests

class Pokemon:
    def __init__(self, name, height, weight, base_experience, abilities, stats, moves, types):
        self.name = name
        self.height = height
        self.weight = weight
        self.base_experience = base_experience
        self.abilities = abilities
        self.stats = stats
        self.moves = moves
        self.types = types

    def P_name(self):
        print(f"Name : {self.name}")

    def P_height(self):
        print(f"Height : {self.height}")

    def P_weight(self):
        print(f"Weight : {self.weight}")

    def P_base_experience(self):
        print(f"Base Experience : {self.base_experience}")

    def P_types(self):
        a = []
        for move in data["types"]:
            a.append(move["type"]["name"])

        b = ", ".join(a)
        print(f"Types : {b} ")

    def P_moves(self):    
        a = []
        for move in data["moves"][:10]:
            a.append(move["move"]["name"])

        b = ", ".join(a)
        print(f"Moves : {b} ")

    def P_stat(self):    
        a = []
        for move in data["stats"]:
            name = move['stat']['name']  
            value = move['base_stat']      
            combined_string = f"{name}: {value}"
            a.append(combined_string)

        b = ", ".join(a)
        print(f"Stats : {b} ")

    def P_abilities(self):    
        a = []
        for move in data["abilities"]:
            a.append(move["ability"]["name"])

        b = ", ".join(a)
        print(f"Abilities : {b} ")

    def P_image(self):
        print(f"Image URL: {data['sprites']['front_default']}")


while True:
    name = input("Enter the name of the pokemon: ").strip().lower()
    url = f"https://pokeapi.co/api/v2/pokemon/{name}"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        k =  Pokemon(data["name"], data["height"], data["weight"], data["base_experience"], data["abilities"], data["stats"], data["moves"], data["types"])
        print()
        k.P_name()
        k.P_height()
        k.P_weight()
        k.P_base_experience()
        k.P_types()
        k.P_moves()
        k.P_stat()
        k.P_abilities()
        k.P_image()
        print()

    else:
        print("Pokémon not found! Check your spelling.")
        break



# -- ./Projects/P12 | Pokemon (Adv).py