def sub(num1, num2):
    if(not (isinstance(num2, (int, float)) and isinstance(num2, (int, float)))):
        raise TypeError("passed value is not a number")
    
    return num1 - num2

def mul(num1, num2):
    return num1 * num2

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
