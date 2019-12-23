import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors


class Board:
    def __init__(self, n):
        self.size = n
        self.grid = np.zeros((n, n), dtype=int)

        self.cmap = colors.ListedColormap(['red', 'blue'])
        self.bounds = [0, 0.5, 1]
        self.norm = colors.BoundaryNorm(self.bounds, self.cmap.N)

    def reset(self):
        self.grid = np.zeros((n, n), dtype=int)

    def placeQueensMulti(self, all=True):
        if all:
            pltSize = int(self.size**0.5)
            ctr = 1
            ctrMax = pltSize**2
            _ = plt.figure(figsize=(10, 8))
            explored = []
            for j in range(self.size):
                self.reset()
                if (self.placeQueens(0, j)) and (ctr <= ctrMax) and (j not in explored):
                    mat = np.array(board.grid)
                    # print(mat)
                    plt.subplot(pltSize, pltSize, ctr)
                    plt.xticks(np.arange(-0.5, self.size), range(0, self.size+1))
                    plt.yticks(np.arange(-0.5, self.size), range(0, self.size+1))
                    plt.imshow(mat, cmap=self.cmap, norm=self.norm)
                    plt.grid(which='major', axis='both', linestyle='-', color='w', linewidth=2)
                    # print(ctr)
                    ctr += 1
                    explored.append(np.argmax(self.grid[0]))
        else:
            self.placeQueens()
            mat = np.array(board.grid)
            print(mat)
            plt.imshow(mat)
            plt.show()
            print("tf")

    def placeQueens(self, start_row=0, j=0):
        i = start_row
        while (i < self.size):
            while (j < self.size):
                if self.isValid(i, j):
                    self.grid[i, j] = 1
                    if i+1 >= self.size or self.placeQueens(i+1):
                        return True
                    else:
                        self.grid[i, j] = 0
                j += 1
            return False

    def isValid(self, row, col):
        # print(self.grid)
        if any([self.grid[row, x] for x in range(self.size)]) or any([self.grid[x, col] for x in range(self.size)]):
            # print("hori/vert")
            return False
        for x in range(self.size):
            if ((0 <= row-x < self.size) and (0 <= col-x < self.size) and self.grid[row-x, col-x]):
                # print((row-x, col-x))
                return False
            if ((0 <= row+x < self.size) and (0 <= col+x < self.size) and self.grid[row+x, col+x]):
                # print((row+x, col+x))
                return False
            if ((0 <= row-x < self.size) and (0 <= col+x < self.size) and self.grid[row-x, col+x]):
                # print((row-x, col+x))
                return False
            if ((0 <= row+x < self.size) and (0 <= col-x < self.size) and self.grid[row+x, col-x]):
                # print((row+x, col-x))
                return False
        return True


if __name__ == "__main__":
    # n = 8
    n = int(input("Enter size N: "))

    board = Board(n)
    # board.placeQueens()
    board.placeQueensMulti()

    plt.show()
