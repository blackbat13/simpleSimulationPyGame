import random
import pygame
# Gdy importujemy zależności z obecnego pakietu, to podajemy pełną ścieżkę
from simulation.elements.element import Element


class Particle(Element):
    """
    Class representing a human in the simulation.
    """

    def __init__(self, parent):
        super().__init__(parent)
        self._position = (random.randint(0, parent.width),
                          random.randint(0, parent.height))
        self._radius = 10
        self._velocity = (random.random() * 10 - 5, random.random() * 10 - 5)
        self._charge = 10.0
        self._mass = 1.0
        self._force = (0.0, 0.0)

    @property
    def charge(self) -> float:
        return self._charge

    @property
    def mass(self) -> float:
        return self._mass

    @property
    def force_x(self) -> float:
        return self._force[0]

    @force_x.setter
    def force_x(self, value: float):
        self._force = (value, self._force[1])

    @property
    def force_y(self) -> float:
        return self._force[1]

    @force_y.setter
    def force_y(self, value: float):
        self._force = (self._force[0], value)

    @property
    def vel_x(self) -> float:
        return self._velocity[0]

    @vel_x.setter
    def vel_x(self, value: float):
        self._velocity = (value, self._velocity[1])

    @property
    def vel_y(self) -> float:
        return self._velocity[1]

    @vel_y.setter
    def vel_y(self, value: float):
        self._velocity = (self._velocity[0], value)

    def draw(self, screen):
        pygame.draw.circle(screen,
                           (255, 0, 0),
                           [self._position[0], self._position[1]],
                           self._radius)

    def update(self):
        self.vel_x += self.force_x / self.mass
        self.vel_y += self.force_y / self.mass
        self._force = (0.0, 0.0)
        self.x += self.vel_x
        self.y += self.vel_y
        if self.x <= 0 or self.x >= self._parent.width:
            self.vel_x *= -1
        if self.y <= 0 or self.y >= self._parent.height:
            self.vel_y *= -1
