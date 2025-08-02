import math

def add(a,b):
    return a+b

def sub(a,b):
    return

def mul(a,b):
    return a*b

def log(a,b):
    if a <= 0:
        raise ValueError("Log Base must be positive")
    if b<= 0:
        raise ValueError('Log arg must be positive')
    return math.log(b,a)

def exp(a,b):
    return a ** b

import math
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError('Error! Cannot divide by 0!')
    return b / a

def log(a, b):
    if not isinstance(a, int) and not isinstance(a, float):
        raise ValueError('Must be an int or float')
    elif not isinstance(b, int) and not isinstance(b, float):
        raise ValueError('Must be an int or float')
    elif a <= 0 or a == 1 or b <= 0:
        if a == 1:
            raise ValueError('Error! Base cannot be 1!')
        elif b == 0:
            raise ZeroDivisionError('Error! Base cannot be 0!')
        else:
            raise ValueError('Error! Argument cannot be 0!')
    return math.log(b, a)


def exp(a, b):
    return a ** b
