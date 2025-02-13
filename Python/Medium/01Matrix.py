from typing import List


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:

        cl = len(mat)
        rowl = len(mat[0])

        memo = {}
        for i in range(cl):
            for j in range(rowl):
                memo[str(i) + ' ' + str(j)] = float('inf')

        def checkN(x, y):

            if mat[x][y] == 0:
                return 0
            else:
                if x + 1 < cl:
                    s = checkN(x + 1, y)
                if y + 1 < rowl:
                    e = checkN(x, y + 1)
                if x - 1 >= 0:
                    n = checkN(x - 1, y)
                if y - 1 >= 0:
                    w = checkN(x, y - 1)

                return min(s, e, n, w) + 1

        dis = []

        for i in range(cl):

            new_row = []

            for j in range(rowl):
                new_row.append(checkN(i, j))

            dis.append(new_row)

        print(mat)
        print(dis)
        return dis