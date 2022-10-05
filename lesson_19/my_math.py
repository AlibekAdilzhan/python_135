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