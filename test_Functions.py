import unittest
import Functions

class TestFunctions(unittest.TestCase):
    def test_add(self):
        self.assertEqual(Functions.add(2,3), 5)
        self.assertEqual(Functions.add(-5,5), 0)
        self.assertEqual(Functions.add(-4,-4), -8)

    def test_subtract(self):
        self.assertEqual(Functions.subtract(2,3), -1)
        self.assertEqual(Functions.subtract(-5,5), -10)
        self.assertEqual(Functions.subtract(-4,-4), 0)

    def test_multiply(self):
        self.assertEqual(Functions.multiply(2,3), 6)
        self.assertEqual(Functions.multiply(-5,5), -25)
        self.assertEqual(Functions.multiply(-4,-4), 16)

    def test_divide(self):
        self.assertEqual(Functions.divide(2,4), 0.5)
        self.assertEqual(Functions.divide(4,-2), -1)
        self.assertEqual(Functions.divide(-4,-4), 1)

    def test_square(self):
        self.assertEqual(Functions.square(11), 121)
        self.assertEqual(Functions.square(0), 0)
        self.assertEqual(Functions.square(-10), 100)


if __name__ == "__main__":
    unittest.main()
