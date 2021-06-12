import pygame
import cell
import sys
import grid


def main():
    pygame.init()
    game = Game()
    game.runGame()


class Game:
    """
    Game Class.
    """

    def __init__(self):
        self.width = 1000
        self.height = 700
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.background = pygame.Surface(self.screen.get_size()).convert()
        self.screen.fill((255, 255, 255))
        self.grid = grid.Grid(self.screen, self.width, self.height)

    """
    Main game class. 
    """
    def runGame(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            pygame.display.update()
            self.screen.fill((255, 255, 255))
            self.grid.draw()


if __name__ == '__main__':
    main()
