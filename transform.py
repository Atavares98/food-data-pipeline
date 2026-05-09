import json 
import os
import csv

os.makedirs("silver", exist_ok=True)

def transform(file, writer):  # recebe o writer como parâmetro
    with open(f"bronze/{file}", "r", encoding="utf-8") as f:
        data = json.load(f)
        for i in data["products"]:
            produto = {
                "categoria": file.split("_")[0],
                "product_name": i.get("product_name"),
                "proteins_100g": i.get("nutriments", {}).get("proteins_100g"),
                "fat_100g": i.get("nutriments", {}).get("fat_100g"),
                "carbohydrates_100g": i.get("nutriments", {}).get("carbohydrates_100g"),
                "energy-kcal_100g": i.get("nutriments", {}).get("energy-kcal_100g"),
                "nutriscore_grade": i.get("nutriscore_grade")
            }
            writer.writerow(produto)

# Abre o CSV uma vez só, fora da função
with open("silver/products.csv", "w", encoding="utf-8") as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=["categoria", "product_name", "proteins_100g", "fat_100g", "carbohydrates_100g", "energy-kcal_100g", "nutriscore_grade"])
    writer.writeheader()  # cabeçalho uma vez só
    for ficheiro in os.listdir("bronze"):
        transform(ficheiro, writer)  # passa o writer a cada chamada

