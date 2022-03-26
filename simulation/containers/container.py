from abc import ABC
from typing import List
from simulation.elements import Element


class Container(ABC):
    """
    Container class.
    """

    def __init__(self, size: (int, int)):
        self._elements: List[Element] = []
        self._size = size

    @property
    def width(self) -> int:
        return self._size[0]

    @property
    def height(self) -> int:
        return self._size[1]

    @width.setter
    def width(self, value: int):
        self._size = (value, self._size[1])

    @height.setter
    def height(self, value: int):
        self._size = (self._size[0], value)

    def draw(self, screen):
        """
        Draw elements.
        :return: None
        """
        for element in self._elements:
            element.draw(screen)

    def update(self):
        """
        Update simulation.
        :return: None
        """
        for element in self._elements:
            element.update()

    def add_element(self, element: Element):
        """
        Adds element to the list.
        :param element: Element to add.
        :return: None.
        """
        self._elements.append(element)
