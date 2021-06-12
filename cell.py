import pygame


class Cell(pygame.sprite.Sprite):
    def __init__(self, screen, xCood, yCood, size):
        self.screen = screen
        self.xCood = xCood
        self.yCood = yCood
        self.size = size
        self.color = (50, 240, 100)
        self.rect = pygame.draw.rect(self.screen, self.color, (self.xCood, self.yCood, self.size, self.size))

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect, 2, border_radius=1)
