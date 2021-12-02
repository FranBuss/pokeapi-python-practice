import requests
import webbrowser

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
            'types' : pokemon_info['types'][0]['type']['name']
        }

        template = f'''
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta http-equiv="X-UA-Compatible" content="IE=edge">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <link rel="stylesheet" href="styles.css">
                <title>{info['name']}</title>
            </head>
            <body>
                <h1>POKEMON</h1>
                <div class="pokeimage">
                <a href="https://pokemon.fandom.com/wiki/{info['name']}" target="_blank"><img src="{info['image']}"></a>
                </div>
                <div class="info">
                    <p><strong>ID: </strong> {info['id']}</p>
                    <p><strong>NAME: </strong>{info['name']}</p>
                    <p><strong>HEIGTH: </strong>{info['height']}</p>
                    <p><strong>BASE EXPERIENCE: </strong>{info['base_experience']}</p>
                    <p><strong>WEIGHT: </strong>{info['weight']}</p>
                    <p><strong>TYPE: </strong>{info['types']}</p>
                </div>
            </body>
            </html>
        '''

        file = open("pokeapi.html","w")
        file.write(template)
        file.close()

def options():
    print("Enter the number of the option... 1-Pokemons Range, 2-Pokemon, 0-EXIT")
    op = int(input(">"))
    while op != 0:

        if op == 1:
            pokemonsLimits()

        elif op == 2:
            pokemon()
            url = "pokeapi.html"
            webbrowser.open_new_tab(url)

        elif op == 0:
            break

if __name__ == '__main__':
    options()
