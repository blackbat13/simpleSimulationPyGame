from abc import ABC
import math


class Element(ABC):
    """
    Abstract class representing single element in the simulation.
    """

    def __init__(self, parent):
        self._parent = parent
        self._position = (0, 0)

    @property
    def x(self) -> int:
        return self._position[0]

    @property
    def y(self) -> int:
        return self._position[1]

    @x.setter
    def x(self, value: int):
        self._position = (value, self._position[1])

    @y.setter
    def y(self, value: int):
        self._position = (self._position[0], value)

    def draw(self, screen):
        pass

    def update(self):
        pass

    def euclidean_distance_to(self, element):
        """
        Compute distance to given element.
        :param element: element to compute distance to.
        :return: Distance, float.
        """
        return math.sqrt((self.x - element.x) ** 2 + (self.y - element.y) ** 2)
