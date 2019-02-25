import math


class Line:
    def __init__(self, c1, c2):
        self.c1 = c1
        self.c2 = c2

    def distance(self):
        x1 = self.c1[0]
        y1 = self.c1[1]
        x2 = self.c2[0]
        y2 = self.c2[1]

        return math.sqrt(((x2 - x1)**2) + ((y2 - y1)**2))

    def slope(self):
        x1 = self.c1[0]
        y1 = self.c1[1]
        x2 = self.c2[0]
        y2 = self.c2[1]

        return (y2 - y1) / (x2 - x1)


coordinate1 = (3, 2)
coordinate2 = (8, 10)
li = Line(coordinate1, coordinate2)
print(li.distance())
print(li.slope())
