class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist(self, point_2):
        d = ((point_2.x - self.x)**2 + (point_2.y - self.y)**2)**0.5
        return d


point_1 = Point(0, 0)
point_2 = Point(3, 4)

d = point_1.dist(point_2)
print(d)