def maxNumber( a, b, c):
    if a >=b and a >= c:
        return a
    elif b >= c:
        return b
    else:
        return c

print(maxNumber(3,7,5))
print(maxNumber(10,10,5))
