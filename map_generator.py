import csv

import defs


class GameMap:
    def __init__(self):
        csv_file = open('./resources/map.csv')
        f = csv.reader(csv_file, delimiter=',', lineterminator='\r\n', skipinitialspace=True)
        self.map = []
        for i, row in enumerate(f):
            self.map.append([int(s) for s in row])
        csv_file.close()

        self.rows = len(self.map)
        self.cols = len(self.map[0])
        print(f'GameMap rows : {self.rows} cols : {self.cols}')
        if self.rows > defs.max_cell_num or self.cols > defs.max_cell_num:
            raise ValueError('self.rows > defs.max_cell_num or self.cols > defs.max_cell_num')
        pass


if __name__ == "__main__":
    GameMap()
    # call the main function
