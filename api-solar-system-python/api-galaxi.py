import requests #let 'u get data from api-url'
# pip install requests
import os #let 'u execute comands'

def diplay():
    print("### Main menu####")
    print("[1]. Planets")
    print("[2]. Moons")
    print("[3]. Stars")
    print("[4]. Asteroid")
    print("[5]. Comets")
    print("[6]. Exit")
    opt = input("::: Press any options:::")
    return opt

def evaluate(option, info):
    if (option == '1'):
        planets = list(filter(lambda x: x['bodyType'] == "Planet", info['bodies']))
        
        for planet in planets:
            print("==============================")
            print("Planet Name:", planet['englishName'])
            print("Inclination:", planet['inclination'])
            print("Gravity:", planet['gravity'])
            print("Is Planet:", planet['isPlanet'])
            print("==============================")

    if option == '2':
        moons = list(filter(lambda x: x['bodyType'] == "Moon", info['bodies']))
    
        for moon in moons:
            print("==============================")
            print("Moon Name:", moon['englishName'])
            print("Inclination:", moon['inclination'])
            print("Gravity:", moon['gravity'])
            print("Is Planet:", moon['isPlanet'])
            print("==============================")

    if option == '3':
        stars = list(filter(lambda x: x['bodyType'] == "Star", info['bodies']))
    
        for star in stars:
            print("==============================")
            print("Star Name:", star['englishName'])
            print("Inclination:", star['inclination'])
            print("Gravity:", star['gravity'])
            print("Is Planet:", star['isPlanet'])
            print("==============================")

    if option == '4':
        asteroids = list(filter(lambda x: x['bodyType'] == "Asteroid", info['bodies']))
    
        for asteroid in asteroids:  
            print("==============================")
            print("Asteroid Name:", asteroid['englishName']) 
            print("Inclination:", asteroid['inclination'])
            print("Gravity:", asteroid['gravity'])
            print("Is Planet:", asteroid['isPlanet'])
            print("==============================")

        
    if option == '5':
        comets = list(filter(lambda x: x['bodyType'] == "Comet", info['bodies']))
    
        for comet in comets:  
            print("==============================")
            print("Comet Name:", comet['englishName']) 
            print("Inclination:", comet['inclination'])
            print("Gravity:", comet['gravity'])
            print("Is Planet:", comet['isPlanet'])
            print("==============================")


def get_data():
    api_url = "https://api.le-systeme-solaire.net/rest/bodies/?filter%5B%5D=isComet"
    
    try:
        response = requests.get(api_url)
        response.raise_for_status() 
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"API error {e}")

os.system("clear")
print(":::Solar System Information:::")
info = get_data()
option = diplay()

while option != '6':
    evaluate(option, info)
    option = diplay()
