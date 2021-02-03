''' 1. Ask for user input
2. Create a dynamic URL based on step 1.
3. Fetch the data from the url in step 2.
4. Convert JSON to a dictionary.
5. Print out pokemon data.



import requests

req = request.get("https://swapi.dev/apu/people/2/")
person = req.json()
print = (f"Name is\t\t\t{person['name']}")
print(f"Birth year is\t\t{person['birth_year]}")

print("Films involved in:")
for film in person['films']:
    req = requests.get(film)
    film = req = requests.get(film)
    print("Film is: ", film['title'])

'''



import requests

pokemon = input("Which Pokemon do you want to find? ")
pokemon = pokemon.lower()

url = f"https://pokeapi.co/api/v2/pokemon/{pokemon}"

req = requests.get(url)

data = req.json()

print(f"Name is\t\t{data['name']}")
print("Abilities:")
for ability in data['abilities']:
    print(ability['ability']['name'])

