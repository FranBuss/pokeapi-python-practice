import requests

def pokemonsLimits():
    try:
        print("*---------------------------------------*")
        print("Enter the first value of pokeAPI:")
        offset = int(input(">"))
        print("*---------------------------------------*")
        print("Enter the limit you want to get:")
        limit = int(input(">"))
        print("*---------------------------------------*")
        
        url  = f"https://pokeapi.co/api/v2/pokemon?limit={limit}&offset={offset}"

        response = requests.get(url)
        if response.status_code == 200:
            
            pokemon_info  = response.json()
            results = pokemon_info.get("results", [])

            counter = 1

            if results:
                for pokemon in results:
                    name = pokemon["name"]
                    print(f"{counter} - {name}")
                    counter += 1
                    
    except:
        print("ERROR -- OnlyNumbers")

def pokemon():

    print("*---------------------------------------*")
    print("Enter the number of the pokemon you want:")
    number = int(input(">"))
    print("*---------------------------------------*")

    url  = f"https://pokeapi.co/api/v2/pokemon/{number}"

    response = requests.get(url)
    if response.status_code == 200:
        
        pokemon_info  = response.json()
        info = {
            "image" : pokemon_info["sprites"]["front_default"],
            "id": pokemon_info["id"],
            "name" : pokemon_info["name"],
            'height' : pokemon_info[ 'height' ],
            'base_experience' : pokemon_info[ 'base_experience' ],
            'weight' : pokemon_info[ 'weight' ],
            'species' : pokemon_info[ 'species' ][ 'name' ]
        }

        print(f"""
        IMAGE: {info['image']} 
        ID: {info['id']}
        NAME: {info['name']}
        HEIGTH: {info['height']}
        BASE EXPERIENCE: {info['base_experience']}
        WEIGHT: {info['weight']}
        SPECIE: {info['species']}
        """)
    

def options():
    print("Enter the number of the option... 1-Pokemons Range, 2-Pokemon")
    op = int(input(">"))
    while op != 0:
        if op == 1:
            pokemonsLimits()
        elif op == 2:
            pokemon()
        elif op == 0:
            break

if __name__ == '__main__':
    options()
