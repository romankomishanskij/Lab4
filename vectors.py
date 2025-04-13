import math # using sqrt(), acos()

class Vector:
    def __init__(self, x : float, y : float) -> None:
        if not (isinstance(x, float) and isinstance(y, float)):
            raise TypeError("Vector coordinates must be number")
        self.x = x
        self.y = y

    def __add__(self, other):
        if not isinstance(other, Vector):
            raise TypeError("You can do only sum of two Vector type objects")

        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        if not isinstance(other, Vector):
            raise TypeError("You can do only substract two Vector type objects")

        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y


        elif isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)

        else:
            raise TypeError("You can multiply vector only with other vector or number")

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        if not isinstance(other, (int, float)):
            raise TypeError("You can devision only by number")
        if other:
            return Vector(self.x / other, self.y / other)

    def __abs__(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def angle_between(self, other):
        if not isinstance(other, Vector):
            raise TypeError("You can get angle only between two vectors")

        res = (self * other) / (abs(self) * abs(other))
        res = max(-1.0, min(1.0, res))

        return math.acos(res)

    def __str__(self):
        return f"vector({self.x}, {self.y})"

    def __repr__(self):
        return f"vector: (x = {self.x}, y = {self.y})"

    def __pow__(self, power):
        raise Exception("You cant powered vector")

    def __eq__(self, other):
        return isinstance(other, Vector) and self.x == other.x and self.y == other.y