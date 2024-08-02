import unittest

def multiply(a,b):
    return a * b

class TestMultiply(unittest.TestCase):
    def test_multipy(self):
        self.assertEqual(multiply(2,3),6)
        self.assertEqual(multiply(-1,1),-1)
        self.assertEqual(multiply(0,0),0)
        


if __name__ == '__main__':
    unittest.main()
