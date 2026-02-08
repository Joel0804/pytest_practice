def add(a, b):
    return a + b 

def div(a, b):
    if b == 0:
        ValueError("Cannot be divided by zero") 
    return a / b