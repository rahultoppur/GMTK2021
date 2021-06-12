import pygame
import grid
import sys

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
        #self.background = self.background.convert()
        self.screen.fill((255,255,255))
        self.gridPiece = grid.Grid(self.screen, 100, 100)
        

    def runGame(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            pygame.display.update()
            self.screen.fill((255,255,255))
            self.gridPiece.draw()

if __name__ == '__main__':
    main()
