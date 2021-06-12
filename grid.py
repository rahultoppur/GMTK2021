import pygame
import cell


class Grid:
    def __init__(self, screen, width, height):
        self.screen = screen
        self.width = width
        self.height = height
        self.SIZE = 50
        self.grid = self.genGrid(self.height, self.width)

    """
    Initialize a grid with the given height and width. 
    """

    def genGrid(self, height, width):
        grid = []
        for i in range(height // self.SIZE):
            col = []
            for j in range(width // self.SIZE):
                col.append(cell.Cell(self.screen, j * self.SIZE, i * self.SIZE, self.SIZE))
            grid.append(col)
        return grid

    """
    Loop through each cell in the grid and render it.
    """

    def draw(self):
        # Loop through grid and call Cell's draw
        for i in range(self.height // self.SIZE):
            for j in range(self.width // self.SIZE):
                self.grid[i][j].draw()
