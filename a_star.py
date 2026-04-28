from queue import PriorityQueue

class AStar:
    def __init__(self, matrix, source, target):
        self.matrix = matrix
        self.source = source
        self.target = target

    def run(self):
        ...