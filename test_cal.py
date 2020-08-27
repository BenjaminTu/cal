import unittest
import random as rand
from cal import *

class MyTest(unittest.TestCase):
    def test(self):
        for i in range(100):
            for j in range(100):
                x = rand.randrange(0, 100)
                y = rand.randrange(0, 100)
                self.assertEqual(add(x, y), x + y)
                self.assertEqual(sub(x, y), x - y)
                self.assertEqual(mul(x, y), x * y)
        print("test passed!")

if __name__ == '__main__':
    unittest.main()
