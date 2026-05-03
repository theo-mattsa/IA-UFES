import math
from queue import PriorityQueue


class Cell:
    def __init__(self, position: tuple[int, int], cost: int = 1):
        self.position = position
        self.cost = cost
        self.h = 0
        self.g = math.inf
        self.f = math.inf

    def calculate_g(self, g_last):
        self.g = g_last + self.cost

    def calculate_h(self, target_position: tuple[int, int], h_func):
        self.h = h_func(self.position, target_position)

    def calculate_f(self):
        self.f = self.g + self.h


class AStar:
    def __init__(self, matrix, source: list | tuple, target: list | tuple, h_func=None):
        self.matrix = matrix
        self.source = tuple(source)
        self.target = tuple(target)

    def run(self): ...
