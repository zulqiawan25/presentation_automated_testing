class Calculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y == 0:
            raise ValueError("Cannot divide by zero")
        return x / y

# Example Usage:
calculator = Calculator()

# Addition
result_add = calculator.add(5, 3)
print(f"Addition Result: {result_add}")

# Subtraction
result_subtract = calculator.subtract(8, 2)
print(f"Subtraction Result: {result_subtract}")

# Multiplication
result_multiply = calculator.multiply(4, 6)
print(f"Multiplication Result: {result_multiply}")

# Division
try:
    result_divide = calculator.divide(10, 2)
    print(f"Division Result: {result_divide}")
except ValueError as e:
    print(f"Error: {e}")
