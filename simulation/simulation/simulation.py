import pygame
from simulation.containers import MagneticField
from simulation.elements import Particle


class Simulation:
    def __init__(self):
        self._open_world = MagneticField((600, 600))
        for _ in range(10):
            self._open_world.add_element(Particle(self._open_world))

    def start(self):
        """
        Starts simulation.
        :return: None.
        """
        pygame.init()

        screen = pygame.display.set_mode((600, 600))
        pygame.display.set_caption("Simple Simulation")
        clock = pygame.time.Clock()
        done = False
        while not done:
            # Main event loop

            # Przechodzimy przez wszystkie zdarzenia
            for event in pygame.event.get():
                # Szukamy zdarzenia wyjścia z programu
                if event.type == pygame.QUIT:
                    done = True

            # Czyścimy ekran
            screen.fill((255, 255, 255))

            # Aktualizujemy stan symulacji
            self._open_world.update()
            # Rysujemy
            self._open_world.draw(screen)

            # Draw new content
            pygame.display.flip()

            # Limit frames to 60 per second
            clock.tick(60)

        pygame.quit()


if __name__ == "__main__":
    # W tym miejscu warto pokazać przykładowe użycie naszej klasy
    simulation = Simulation()
    simulation.start()
