import random

def create_nick(name, surname):
    n = random.randint(0, 10000)
    nick = f"{name}_{surname}_{n}"
    return nick

def square_area(a):
    s = a**2
    return s

def triangle_area(h, b):
    s = 1 / 2 * h * b
    return s

def rectangle_area(a, b):
    s = a * b
    return s

