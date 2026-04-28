import json
import numpy as np

def open_json_file(path: str):
    with open(path, 'r') as file:
        data = json.load(file)
    return data

def main():
    map_data = open_json_file('./map.json')
    matrix = np.array(map_data['matrix'])
    print(matrix)




main()