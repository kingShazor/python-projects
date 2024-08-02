count = 0
with open("data.txt", 'r') as file:
    for line in file:
        count += 1

print(f"data.txt hat {count} Zeilen!")
