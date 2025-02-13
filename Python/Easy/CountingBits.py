from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        counter = [0] * (n + 1)
        for i in range(n + 1):
            counter[i] = counter[i >> 1] + i % 2

        return counter
