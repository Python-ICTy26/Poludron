import pathlib
import random
import typing as tp

import pygame
from pygame.locals import *

Cell = tp.Tuple[int, int]
Cells = tp.List[int]
Grid = tp.List[Cells]


class GameOfLife:
    def __init__(
        self,
        size: tp.Tuple[int, int],
        randomize: bool = True,
        max_generations: tp.Optional[float] = float("inf"),
    ) -> None:
        # Размер клеточного поля
        self.rows, self.cols = size
        # Предыдущее поколение клеток
        self.prev_generation = self.create_grid()
        # Текущее поколение клеток
        self.curr_generation = self.create_grid(randomize=randomize)
        # Максимальное число поколений
        self.max_generations = max_generations
        # Текущее число поколений
        self.generations = 1

    def create_grid(self, randomize: bool = False) -> Grid:
        if randomize == True:
            return [[random.randint(0,1) for _ in range(self.cols)] for _ in range(self.rows)]
        else:
            return [[0 for _ in range(self.cols)] for _ in range(self.rows)]

    def get_neighbours(self, cell: Cell) -> Cells:
        # Copy from previous assignment
        row, col = cell
        neighbours = []
        positions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

        for i in positions:
            row_pos, col_pos = row + i[0], col + i[1]
            if row_pos < 0 or row_pos >= self.rows or col_pos < 0 or col_pos >= self.cols:
                continue
            else:
                neighbours.append(self.curr_generation[row_pos][col_pos])
        return neighbours


    def get_next_generation(self) -> Grid:
        # Copy from previous assignment
        pass

    def step(self) -> None:
        """
        Выполнить один шаг игры.
        """
        pass

    @property
    def is_max_generations_exceeded(self) -> bool:
        """
        Не превысило ли текущее число поколений максимально допустимое.
        """
        pass

    @property
    def is_changing(self) -> bool:
        """
        Изменилось ли состояние клеток с предыдущего шага.
        """
        pass

    @staticmethod
    def from_file(filename: pathlib.Path) -> "GameOfLife":
        """
        Прочитать состояние клеток из указанного файла.
        """
        pass

    def save(self, filename: pathlib.Path) -> None:
        """
        Сохранить текущее состояние клеток в указанный файл.
        """
        pass
