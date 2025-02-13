from collections import Counter


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        n = Counter(nums)

        for v in n.values():
            if v > 1:
                return True
        return False

