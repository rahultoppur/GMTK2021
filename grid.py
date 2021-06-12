import pygame

class Grid(pygame.sprite.Sprite):
    def __init__(self, screen, xCood, yCood):
        self.screen = screen 
        self.xCood = xCood
        self.yCood = yCood
        self.color = (50, 240, 100)
        self.rect = pygame.draw.rect(self.screen, self.color, (self.xCood, self.yCood, 50, 50))

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
