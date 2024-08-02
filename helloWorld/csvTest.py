import csv

products = [
    ["Name", "Preis"],
    ["Schrauben", 3.49],
    ["Zughilfe", 12.90],
    ["Booster", 8.90]
]

with open("products.csv", 'w') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(products)

with open("products.csv", 'r') as csvFile:
    reader = csv.reader(csvFile)
    for line in reader:
        print(line)
