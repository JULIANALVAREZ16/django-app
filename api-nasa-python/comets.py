import requests
import os


def get_comet_data(api_key):
    print(":::COMETS INFORMATION::") 
    api_url = f"https://api.nasa.gov/neo/rest/v1/neo/3726712?api_key={api_key}"


    try:
        response = requests.get(api_url)
        response.raise_for_status()
        data = response.json()

        # show 
        os.system('clear')
        print("=====COMET INFORMATION======")
        #comet name
        print(f"Comet Name:{data['name']}")
        #Absolute magnitude
        print(f"Absolute magnitude:{data['absolute_magnitude_h']}")
        #Estimated diameter max (KM)
        print(f"Estimated diameter max (KM):{data['estimated_diameter']['kilometers']['estimated_diameter_max']}")

        #Estimated diameter min (KM)
        print(f"Estimated diameter min (KM):{data['estimated_diameter']['kilometers']['estimated_diameter_min']}")

        #Estimated diameter max (FT)
        print(f"Estimated diameter max (FT):{data['estimated_diameter']['feet']['estimated_diameter_max']}")

        #Estimated diameter min (FT)
        print(f"Estimated diameter min (FT):{data['estimated_diameter']['feet']['estimated_diameter_min']}")

    

        #last_observation_date
        print(f"Observation data:{data['orbital_data']['last_observation_date']}")



    except requests.exceptions.RequestException as e:
        print(f"API error: {e}")

api_key_nasa ='S6L0JEg2Vkz5U96aiYNepFetlnsyrPNlHj5vBLWy'
get_comet_data(api_key_nasa)
