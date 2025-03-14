class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

# Creating an object of the class and passing values
calc = Calculator(3, 5)
result = calc.add()
print("Sum:", result)
