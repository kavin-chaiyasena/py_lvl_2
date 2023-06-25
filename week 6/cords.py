import math
class RectangularCoordinates:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def coordinates(self):
        return (self.x, self.y)

    def is_x_or_y(self) -> bool:
        if self.x == 0 or self.y == 0 :
            return True
        else :
            return False


    def quadrant(self):
        if self.x == 0 or self.y == 0:
            return "ไม่ได้อยู่ในจตุภาคใด"
        elif self.x > 0 and self.y > 0:
            return "จตุภาค 1"
        elif self.x < 0 and self.y > 0:
            return "จตุภาค 2"
        elif self.x < 0 and self.y < 0:
            return "จตุภาค 3"
        else:
            return "จตุภาค 4"

    def x_distance(self):
        return abs(self.y)

    def y_distance(self):
        return abs(self.x)

    def distance_from_origin(self):
        self.c = self.x ** 2 + self.y ** 2
        return math.sqrt(self.c)

cords = RectangularCoordinates(0,0)