def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

def truncated_division(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a // b

def modulus(a, b):
    if b == 0:
        return "Error: Modulus by zero"
    return a % b

def exponentiation(a, b):
    return a ** b


a = 10.5
b = 2.5
print(f"Addition: {add(a, b)}")
print(f"Subtraction: {subtract(a, b)}")
print(f"Multiplication: {multiply(a, b)}")
print(f"Division: {divide(a, b)}")
print(f"Truncated Division: {truncated_division(a, b)}")
print(f"Modulus: {modulus(a, b)}")
print(f"Exponentiation: {exponentiation(a, b)}")
