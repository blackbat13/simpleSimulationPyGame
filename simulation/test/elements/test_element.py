import unittest
from simulation.elements import Element


class ElementTestSuite(unittest.TestCase):
    def test_distance_y(self):
        element1 = Element(parent=None)
        element2 = Element(parent=None)
        element2.y = 10
        distance = element1.euclidean_distance_to(element2)
        self.assertEqual(10, distance)

    def test_distance_x(self):
        element1 = Element(parent=None)
        element2 = Element(parent=None)
        element2.x = 10
        distance = element1.euclidean_distance_to(element2)
        self.assertEqual(10, distance)


if __name__ == "__main__":
    unittest.main()
