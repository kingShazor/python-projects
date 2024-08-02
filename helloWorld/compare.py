epsilon=1e-10
num = float(input("Gib die erste Zahl ein: "))
othNum = float(input("Gib die zweite Zahl ein: "))
sum = num + othNum
if abs(num - othNum) < epsilon:
    print("Die Zahlen sind nahezu gleich")
elif num > othNum:
    print("Die erste Zahl ist größer als die Zweite!")
else:
    print("die erste Zahl ist nicht größer als die Zweite!")
