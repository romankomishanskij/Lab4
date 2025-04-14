# Vector Class (2D) in Python

A simple and extensible `Vector` class for working with 2D vectors.  
Includes support for arithmetic operations, dot product, magnitude, normalization, and angle calculation.

---

## Features

- Vector addition and subtraction
- Scalar multiplication and division
- Dot product
- Magnitude (Euclidean norm)
- Normalization (unit vector)
- Angle between two vectors (in radians)
- Operator overloading: `+`, `-`, `*`, `/`, `==`, `abs()`, `-vector`



## Example Usage

```python
from vectors import Vector

v1 = Vector(3, 4)
v2 = Vector(1, 2)

print(v1 + v2)            # vector(4, 6)
print(v1 * 2)             # vector(6, 8)
print(v1 * v2)            # 11 (dot product)
print(abs(v1))            # 5.0
print(v1.normalize())     # vector(0.6, 0.8)
print(v1.angle_between(v2))  # angle in radians
