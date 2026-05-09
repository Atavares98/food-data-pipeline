import requests
import json
import os
from datetime import date

#Criar pasta bronze
os.makedirs("bronze", exist_ok=True)


def categoria(categoria):
    try:
        url = f"https://world.openfoodfacts.org/api/v2/search?categories_tags=en:{categoria}&page_size=1000"
        headers = {"User-Agent": "food-data-pipeline/1.0 (andretavaresreis@gmail.com)"}
        response = requests.get(url, headers=headers)

        response.raise_for_status()

        print(response.status_code)
        print(response.text[:500])
        response_json = response.json()

        with open(f"bronze/{categoria}_{date.today()}_raw.json", "w") as f:
            json.dump(response_json, f)
    
    except requests.exceptions.RequestException as e:
        print(f"Erro com a API {e}")

categoria("meats")






