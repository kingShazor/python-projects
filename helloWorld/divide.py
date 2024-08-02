try:
    number = int(input("Geben sie eine Zahl ein:"))
    divisor = int(input("Geben Sie den Divisor ein:"))
    result = number / divisor
    print(f"{number} geteilt durch {divisor} ergibt {result}")
except ZeroDivisionError:
    print("Eine Division durch 0 ist nicht erlaubt!")
except ValueError:
    print("Geben Sie bitte eine Ganzzahl ein!")

