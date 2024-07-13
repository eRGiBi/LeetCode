class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        r = len(grid)
        c = len(grid[0])

        i = [[float('inf') for _ in range(c)] for _ in range(r)]

        def rot(x, y, v):
            print(x, y, v)
            if x < 0 or y < 0 or x >= r or y >= c or grid[x][y] == 0 or grid[x][y] == 2:
                return

            if grid[x][y] == 1 and i[x][y] > v:
                i[x][y] = v

                rot(x + 1, y, v + 1)
                rot(x - 1, y, v + 1)
                rot(x, y + 1, v + 1)
                rot(x, y - 1, v + 1)

        for row in range(r):
            for col in range(c):
                if grid[row][col] == 2:
                    i[row][col] = 0
                    rot(row, col, 1)

        print(i)

        ma = max([max(row) for row in grid])
        if ma != 0:
            return ma
        return -1

