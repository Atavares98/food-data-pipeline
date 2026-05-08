import requests
import json
import os

#Criar pasta bronze
os.makedirs("bronze", exist_ok=True)

#importar a API
url = "https://world.openfoodfacts.org/api/v2/search?categories_tags=en:meats&page_size=100"

#Colocar numa variável e no formato json
headers = {"User-Agent": "food-data-pipeline/1.0 (andretavaresreis@gmail.com)"}
response = requests.get(url, headers=headers)


print(response.status_code)
print(response.text[:500])
response_json = response.json()

with open("bronze/products_raw.json", "w") as f:
    json.dump(response_json, f)





