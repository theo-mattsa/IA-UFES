import json
import math
from a_star import AStar

HEURISTIC_FUNCTIONS = {
    "euclidian": lambda a, b: math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2),
    "manhattan": lambda a, b: abs(a[0] - b[0]) + abs(a[1] - b[1]),
}


def main():
    with open("map.json", "r") as file:
        data = json.load(file)

    h_func = HEURISTIC_FUNCTIONS.get(data["h_func"], None)
    a_star = AStar(data["matrix"], data["source"], data["target"], h_func)


if __name__ == "__main__":
    main()
