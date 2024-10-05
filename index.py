import unittest


# Your original functions
def add(x, y):
    return x + y

def sub(x, y):
    return x - y

# Unit test class inheriting from unittest.TestCase
class TestMathFunctions(unittest.TestCase):

    def test_add(self):
        # Testing the add function
        self.assertEqual(add(4, 5), 9)  # 4 + 5 should be 9
        self.assertEqual(add(-1, 1), 0) # -1 + 1 should be 0
        self.assertEqual(add(0, 0), 0)  # 0 + 0 should be 0

    def test_sub(self):
        # Testing the sub function
        self.assertEqual(sub(5, 3), 2)  # 5 - 3 should be 2
        self.assertEqual(sub(-1, 1), -2) # -1 - 1 should be -2
        self.assertEqual(sub(0, 0), 0)   # 0 - 0 should be 0

# Run the tests
if __name__ == '__main__':
    unittest.main()
