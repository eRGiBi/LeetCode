from math import floor


class Solution:
    def mySqrt(self, x: int) -> int:
        a = x
        x = 10

        for i in range(100):
            x = (x + a / x) / 2

        return floor(x)


