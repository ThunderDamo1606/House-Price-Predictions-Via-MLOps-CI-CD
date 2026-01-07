import pandas as pd
import sys

df = pd.read_csv("data/housing.csv")

if df.isnull().sum().sum() > 0:
    print(" Missing values found!")
    sys.exit(1)

if (df["price"] <= 0).any():
    print(" Invalid price values!")
    sys.exit(1)

print("✔ Data validation passed")
