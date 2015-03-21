import Point
import math

class Circle(Point):
    def __init__(self, radius, x = 0, y = 0):
        super().__init__(x, y)
        self.radius = radius

    def edge_distance_from_origin(self):
        return abs(self.distance_from_origin() - self.radius)

    def area(self):
        return math.pi * (self.radius ** 2)

    def circumference(self):
        return 2 * math.pi * self.radius

    def __eq__(self, other):
        return self.radius == other.radius and super().__eq__(other)

    def __repr__(self):
        return "Circle({0.radius ! r}, {0.x ! r}, {0.y ! r})".foramt(self)

    def __str__(slef):
        return repr(self)
    
    
