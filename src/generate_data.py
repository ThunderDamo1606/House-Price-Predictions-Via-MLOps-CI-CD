import csv
import random

filename = "data/housing.csv"

with open(filename, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["area", "bedrooms", "age", "price"])

    for i in range(1000):
        area = random.randint(700, 5000)
        bedrooms = random.randint(1, 6)
        age = random.randint(1, 25)

        # simple price formula (realistic)
        price = (area * 450) + (bedrooms * 120000) - (age * 15000)

        writer.writerow([area, bedrooms, age, int(price)])

print("✔ 1000 records written to data/housing.csv")
