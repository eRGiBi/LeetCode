class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:

        def dfs(sx: int, sy: int, tx: int, ty: int):
            if sx == tx and sy == ty:
                return True
            elif sx > tx or sy > ty:
                return False
            else:
                return dfs(sx + sy, sy, tx, ty) or dfs(sx, sy + sx, tx, ty)

        return dfs(sx, sy, tx, ty)


if __name__ == '__main__':
    sol = Solution()
    print(sol.reachingPoints(35, 13, 455955547, 420098884))
