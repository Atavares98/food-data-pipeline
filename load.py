import csv
import psycopg2

def to_decimal(value):
    if value == "" or value is None:
        return None
    return float(value)

conn = psycopg2.connect(
    host="localhost",
    port=5432,
    database="fooddata",
    user="andre",
    password="password123"
)

cur = conn.cursor()
cur.execute("""
    CREATE TABLE IF NOT EXISTS products (
        categoria TEXT, 
        product_name TEXT,
        proteins_100g DECIMAL,
        fat_100g DECIMAL,
        carbohydrates_100g DECIMAL,
        energy_kcal_100g DECIMAL,
        nutriscore_grade TEXT
    )      
""")

conn.commit()

with open("silver/products.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for i in reader:
        cur.execute("""
            INSERT INTO products (categoria, product_name, proteins_100g, fat_100g, carbohydrates_100g, energy_kcal_100g, nutriscore_grade)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (
            i["categoria"],
            i["product_name"],
            to_decimal(i["proteins_100g"]),
            to_decimal(i["fat_100g"]),
            to_decimal(i["carbohydrates_100g"]),
            to_decimal(i["energy-kcal_100g"]),
            i["nutriscore_grade"]
        ))

conn.commit()