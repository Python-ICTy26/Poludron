import pygame
from life import GameOfLife
from pygame.locals import *
from ui import UI


class GUI(UI):
    def __init__(self, life: GameOfLife, cell_size: int = 10, speed: int = 10) -> None:
        super().__init__(life)
        self.speed = speed
        self.width = life.rows * cell_size
        self.height = life.cols * cell_size
        self.cell_size = cell_size
        self.screen = pygame.display.set_mode((self.width, self.height))

    def draw_lines(self) -> None:
        # Copy from previous assignment
        for x in range(0, self.width, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color("black"), (x, 0), (x, self.height))
        for y in range(0, self.height, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color("black"), (0, y), (self.width, y))

    def draw_grid(self) -> None:
        # Copy from previous assignment
        for x in range(self.life.rows):
            for y in range(self.life.cols):
                pygame.draw.rect(
                    self.screen,
                    pygame.Color("green") if self.life.curr_generation[x][y] == 1 else pygame.Color("white"),
                    (
                        y * self.cell_size,
                        x * self.cell_size,
                        self.cell_size,
                        self.cell_size,
                    ),
                )

    def run(self) -> None:
        # Copy from previous assignment
        pass
