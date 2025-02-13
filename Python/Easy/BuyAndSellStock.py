import sys
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = sys.maxsize
        sell = 0

        for i in prices:
            buy = min(buy, prices[i])
            sell = max(sell, prices[i] - buy)

        return sell

class Solution2:
    def maxProfit(self, prices: List[int]) -> int:

        minPrice, maxProfit  = float('inf'), 0

        for price in prices:
            if price < minPrice:
                minPrice = price

            elif price - minPrice > maxProfit:
                maxProfit = price - minPrice

        return maxProfit