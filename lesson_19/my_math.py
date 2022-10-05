import random


def factorial(n):
    s = 1
    for i in range(1, n + 1):
        s *= i
    return s


def circle_area(r):
    s = 3.1415 * r**2
    return s


def derivative(a, n): # a^n -> n*a^(n-1)
    return n * a**(n - 1)


def create_random_list(n):
    a = []
    for i in range(n):
        rv = random.randint(-100, 100)
        a.append(rv)
    return a


HEIGHT = 520
WIDTH = 800
COLOR = (120, 0, 0)

hero = {"height" : 180, "age": 28, "name": "Groznyi"}

if __name__ == "__main__":
    print("hi hi hi")