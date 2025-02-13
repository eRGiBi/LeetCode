from math import comb


def climbStairs(n: int) -> int:
    res = 1
    for i in range(n):
        res += comb(n - 1, i + 1)
        n = n - 1
    return res


if __name__ == '__main__':
    print(climbStairs(4))
