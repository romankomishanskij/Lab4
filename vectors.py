"""
vector.py — A module for working with 2D vectors.

This module defines a `Vector` class that provides a simple and intuitive interface
for performing operations on two-dimensional vectors. It includes functionality for:

- Vector addition and subtraction
- Scalar multiplication and division
- Dot product calculation
- Magnitude (length) computation
- Vector normalization
- Angle calculation between two vectors

Operator overloading allows using standard Python syntax for vector arithmetic:
    - `+`, `-` for addition and subtraction
    - `*` for scalar multiplication and dot product
    - `/` for scalar division
    - `==` for vector equality
    - `abs()` to get vector magnitude
    - `-vector` to reverse vector direction

Raises:
    - `TypeError` when operands are of invalid type
    - `ZeroDivisionError` when dividing by zero
    - `NotImplementedError` for unsupported operations like exponentiation

Example usage:
    >>v1 = Vector(3, 4)
    >>v2 = Vector(1, 2)
    >> v1 + v2
    vector: (x = 4, y = 6)
    >> abs(v1)
    5.0
    >> v1.normalize()
    vector: (x = 0.6, y = 0.8)
"""

import math  # using sqrt(), acos()

class Vector:
    """
    Class for working with 2D vectors.

    Supports basic arithmetic operations, scalar multiplication,
    calculating vector length and angle between vectors.
    """

    def __init__(self, x: float, y: float) -> None:
        """
        Initialize a 2D vector.

        Args:
            x (float or int): X-coordinate of the vector.
            y (float or int): Y-coordinate of the vector.

        Raises:
            TypeError: If either x or y is not a number.
        """
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("Vector coordinates must be numbers")
        self.x = x
        self.y = y

    def __str__(self) -> str:
        """
        Return a human-readable string representation of the vector.

        Returns:
            str: Formatted string.
        """
        return f"vector({self.x}, {self.y})"

    def __repr__(self) -> str:
        """
        Return a detailed string representation of the vector.

        Returns:
            str: Detailed string with component names.
        """
        return f"vector: (x = {self.x}, y = {self.y})"

    def __add__(self, other: object) -> 'Vector':
        """
        Add two vectors.

        Args:
            other (Vector): Another vector.

        Raises:
            TypeError: If other is not a Vector.

        Returns:
            Vector: Resulting vector from addition.
        """
        if not isinstance(other, Vector):
            raise TypeError("You can do only sum of two Vector type objects")
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: object) -> 'Vector':
        """
        Subtract two vectors.

        Args:
            other (Vector): Another vector.

        Raises:
            TypeError: If other is not a Vector.

        Returns:
            Vector: Resulting vector from subtraction.
        """
        if not isinstance(other, Vector):
            raise TypeError("You can do only subtract two Vector type objects")
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: object) -> 'Vector' or float:
        """
        Multiply vector by scalar or compute dot product.

        Args:
            other (int, float, Vector): A number for scaling or another vector for dot product.

        Raises:
            TypeError: If other is not a number or Vector.

        Returns:
            Vector or float: Scaled vector or dot product.
        """
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        elif isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        else:
            raise TypeError("You can multiply vector only with other vector or number")

    def __rmul__(self, other: object) -> 'Vector' or float:
        """
        Right-side multiplication support.

        Args:
            other (int, float, Vector): Scalar or Vector.

        Returns:
            object: Result of multiplication.
        """
        return self.__mul__(other)

    def __truediv__(self, other: float) -> 'Vector':
        """
        Divide vector by a scalar.

        Args:
            other (int, float): Scalar number.

        Raises:
            TypeError: If other is not a number.
            ZeroDivisionError: If division by zero is attempted.

        Returns:
            Vector: Scaled vector.
        """
        if not isinstance(other, (int, float)):
            raise TypeError("You can divide only by number")
        if other == 0:
            raise ZeroDivisionError("Division by zero is not allowed")
        return Vector(self.x / other, self.y / other)

    def __abs__(self) -> float:
        """
        Compute the magnitude (length) of the vector.

        Returns:
            float: Euclidean norm.
        """
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def __pow__(self, power: int) -> None:
        """
        Power operation is not supported for vectors.

        Raises:
            NotImplementedError: Always.
        """
        raise NotImplementedError("Vector power operation is not supported")

    def __eq__(self, other: object) -> bool:
        """
        Check equality of two vectors.

        Args:
            other (object): Another object to compare.

        Returns:
            bool: True if other is a Vector with same components.
        """
        return isinstance(other, Vector) and self.x == other.x and self.y == other.y

    def __neg__(self) -> object:
        """
        Changes the direction of the vector

        Returns:
            Vector: vector with opposites coordinates (-x and -y)
        """
        return Vector(self.x * (-1), self.y * (-1))

    def angle_between(self, other: object) -> float:
        """
        Calculate the angle between this vector and another in radians.

        Args:
            other (Vector): Another vector.

        Raises:
            TypeError: If other is not a Vector.

        Returns:
            float: Angle in radians between the vectors.
        """
        if not isinstance(other, Vector):
            raise TypeError("You can get angle only between two vectors")

        res = (self * other) / (abs(self) * abs(other))
        res = max(-1.0, min(1.0, res))

        return math.acos(res)

    def normalize(self) -> object:
        """
        Normalize the vector (keep direction, set magnitude to 1).

        Returns:
            Vector: A unit vector with the same direction.

        Raises:
            ZeroDivisionError: If the vector is zero.
        """

        mod = abs(self)
        if mod:
            return Vector(self.x / mod, self.y / mod)
        raise ZeroDivisionError("module of vector = 0")

if __name__ == "__main__":
    v1 = Vector(3, 4)
    v2 = Vector(1, 2)

    print("v1:", v1)
    print("v2:", v2)

    print("Addition:", v1 + v2)
    print("Subtraction:", v1 - v2)
    print("Dot Product:", v1 * v2)
    print("Scalar Multiplication:", v1 * 2)
    print("Scalar Division:", v1 / 2)
    print("Magnitude of v1:", abs(v1))
    print("Normalized v1:", v1.normalize())
    print("Angle between v1 and v2 (radians):", v1.angle_between(v2))
    print("Equality check:", v1 == v2)
    print("Negation of v1:", -v1)

