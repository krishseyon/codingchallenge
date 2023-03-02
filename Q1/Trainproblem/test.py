import unittest
from main import *
from main import  solve
class TestTrainProblem(unittest.TestCase):
    def test_calculate_distance(self):
        # Test case 1: A-B-C
        self.assertEqual(calculate_distance(['A', 'B', 'C']), 9)

        # Test case 2: A-D
        self.assertEqual(calculate_distance(['A', 'D']), 5)

        # Test case 3: A-D-C
        self.assertEqual(calculate_distance(['A', 'D', 'C']), 13)

        # Test case 4: A-E-B-C-D
        self.assertEqual(calculate_distance(['A', 'E', 'B', 'C', 'D']), 22)

        # Test case 5: A-E-D
        self.assertEqual(calculate_distance(['A', 'E', 'D']), 'NO SUCH ROUTE')

    # def test_count_trips_with_max_stops(self):
    #     # Test case 6: Trips starting at C and ending at C with a maximum of 3 stops
    #     self.assertEqual(count_trips_with_max_stops('C', 'C', 3), 2)
    #
    # def test_count_trips_with_exact_stops(self):
    #     # Test case 7: Trips starting at A and ending at C with exactly 4 stops
    #     self.assertEqual(count_trips_with_exact_stops('A', 'C', 4), 3)
    #
    # def test_shortest_path(self):
    #     # Test case 8: Shortest route from A to C
    #     self.assertEqual(shortest_path('A', 'C'), 9)

if __name__ == '__main__':
    unittest.main()
