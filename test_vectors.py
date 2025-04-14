from vectors import Vector # for testing
import math
import unittest

class TestVector(unittest.TestCase):
    def setUp(self):
        self.v1 = Vector(3, 4)
        self.v2 = Vector(1, 2)
        self.zero = Vector(0, 0)

    def test_str_and_repr(self):
        self.assertEqual(str(self.v1), "vector(3, 4)")
        self.assertEqual(repr(self.v1), "vector: (x = 3, y = 4)")

    def test_addition(self):
        self.assertEqual(self.v1 + self.v2, Vector(4, 6))

    def test_subtraction(self):
        self.assertEqual(self.v1 - self.v2, Vector(2, 2))

    def test_scalar_multiplication(self):
        self.assertEqual(self.v1 * 2, Vector(6, 8))
        self.assertEqual(2 * self.v1, Vector(6, 8))
        self.assertEqual(self.v1 * self.v2, 11)

    def test_dot_product(self):
        self.assertEqual(self.v1 * self.v2, 11)

    def test_division(self):
        self.assertEqual(self.v1 / 2, Vector(1.5, 2.0))
        with self.assertRaises(ZeroDivisionError):
            self.v1 / 0

    def test_abs(self):
        self.assertEqual(abs(self.v1), 5.0)

    def test_equality(self):
        self.assertTrue(self.v1 == Vector(3, 4))
        self.assertFalse(self.v1 == self.v2)

    def test_negation(self):
        self.assertEqual(-self.v1, Vector(-3, -4))

    def test_angle_between(self):
        expected = math.acos((3 * 1 + 4 * 2) / (5 * math.sqrt(5)))
        self.assertAlmostEqual(self.v1.angle_between(self.v2), expected)

    def test_normalize(self):
        norm = self.v1.normalize()
        self.assertAlmostEqual(norm.x, 0.6)
        self.assertAlmostEqual(norm.y, 0.8)
        with self.assertRaises(ZeroDivisionError):
            self.zero.normalize()

    def test_invalid_operations(self):
        with self.assertRaises(TypeError):
            self.v1 + 5
        with self.assertRaises(TypeError):
            self.v1 - "a"
        with self.assertRaises(TypeError):
            self.v1 * "x"
        with self.assertRaises(TypeError):
            self.v1 / "number"
        with self.assertRaises(NotImplementedError):
            self.v1 ** 2

if __name__ == "__main__":
    unittest.main()