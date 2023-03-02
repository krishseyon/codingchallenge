import unittest

from main import Rover

class TestRover(unittest.TestCase):

    def test_move(self):
        rover = Rover(1, 2, 'N')
        plateau = [5, 5]
        rover.move('L', plateau)
        self.assertEqual(rover.direction, 'W')
        rover.move('R', plateau)
        self.assertEqual(rover.direction, 'N')
        rover.move('M', plateau)
        self.assertEqual(rover.y, 3)
        rover.move('M', plateau)
        self.assertEqual(rover.y, 4)

if __name__ == '__main__':
    unittest.main()
