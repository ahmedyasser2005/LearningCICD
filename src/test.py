import unittest
from main import calcSum


class TestMain(unittest.TestCase):
    def test_calcSum_positive(self):
        self.assertEqual(calcSum(2, 3), 5)

    def test_calcSum_one_negative(self):
        self.assertEqual(calcSum(-1, 3), 0)

    def test_calcSum_both_negative(self):
        self.assertEqual(calcSum(-1, -1), 0)

    def test_calcSum_zero(self):
        self.assertEqual(calcSum(0, 0), 0)


if __name__ == "__main__":
    unittest.main()
