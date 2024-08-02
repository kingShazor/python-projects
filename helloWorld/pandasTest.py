import pandas as pd

data = {
    "Produkt": ["Apfel", "Birne", "Orange"],
    "Preis": [1.20, 0.99, 1.2],
    "Anzahl": [10, 20, 15]
}
df = pd.DataFrame(data)
df["Gesammtwert: "] = df["Preis"] * df["Anzahl"]
print(df)
