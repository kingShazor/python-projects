class rectangle:
    def __init__ (self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2* (self.length + self.width)


rect = rectangle(7, 9)

print(f"Die Fläche ist: {rect.area()}")
print(f"Der Umfang ist: {rect.perimeter()}")
