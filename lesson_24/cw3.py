class Vector_3D:
    def __init__(self, x1, x2, x3):
        self.x1 = x1
        self.x2 = x2
        self.x3 = x3

    def get_length(self):
        l = (self.x1**2 + self.x2**2 + self.x3**2)**0.5
        return l

    def __add__(self, v2):
        v3 = Vector_3D(self.x1 + v2.x1, self.x2 + v2.x2, self.x3 + v2.x3)
        return v3

    def __mul__(self, v2):
        c = self.x1 * v2.x1 + self.x2 * v2.x2 + self.x3 * v2.x3
        return c

    def __str__(self):
        return f"{self.x1} {self.x2} {self.x3}"


v1 = Vector_3D(1, 3, 4)
# v2 = Vector_3D(3, 4, 0)
# v3 = v1 + v2
# print(v1 * v2)
# v3 = v1.__add__(v2)
print(v1)