import unittest

from main import startProject

class TestParkingLot(unittest.TestCase):
    def test_parkinglot(self):

        result = startProject(1, 1, 3)
        self.assertEqual(result)  # add assertion here


if __name__ == '__main__':
    unittest.main()
