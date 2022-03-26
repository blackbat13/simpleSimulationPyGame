from simulation.containers.container import Container
from simulation.elements import Particle
from typing import List


class MagneticField(Container):
    """
    Main container in the simulation.
    """

    def __init__(self, size: (int, int)):
        super().__init__(size)

    def update(self):
        particles: List[Particle] = list(filter(lambda el: isinstance(el, Particle), self._elements))

        for i in range(len(particles)):
            for j in range(i + 1, len(particles)):
                particle1 = particles[i]
                particle2 = particles[j]
                distance = particle1.euclidean_distance_to(particle2)
                if distance == 0:
                    continue

                force = -1 * particle1.charge * particle2.charge / (distance * distance)
                if force > 1000:
                    force = 1000

                diff_x = particle2.x - particle1.x
                diff_y = particle2.y - particle1.y
                force_x = force * diff_x / distance
                force_y = force * diff_y / distance

                particle1.force_x += force_x
                particle1.force_y += force_y
                particle2.force_x -= force_x
                particle2.force_y -= force_y

        super().update()
