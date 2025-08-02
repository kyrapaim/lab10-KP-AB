import math

def add(a,b):
    return a+b

def sub(a,b):
    return

def mul(a,b):
    return a*b

def div(a,b):
    if a == 0:
        raise ZeroDivisionError
    return b/a

def log(a,b):
    if a <= 0:
        raise ValueError("Log Base must be positive")
    if b<= 0:
        raise ValueError('Log arg must be positive')
    return math.log(b,a)

def exp(a,b):
    return a ** b


