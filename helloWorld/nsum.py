maxNumber = int(input("Geben Sie eine Ganzzahl ein:"))
sum = 0
for i in range(1,maxNumber + 1):
    sum += i

print(f"Die Summe aller Zahlen von 1 bis {maxNumber} ist {sum}")
