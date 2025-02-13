from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        lp = nums[0]
        for i in range(len(nums)):
            curr_p = 1
            for j in range(i, len(nums)):
                curr_p *= nums[j]
                lp = max(curr_p, lp)

        return lp

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        prefix, suffix, max_so_far = 0, 0, float('-inf')
        for i in range(len(nums)):
            prefix = (prefix or 1) * nums[i]
            suffix = (suffix or 1) * nums[~i]
            max_so_far = max(max_so_far, prefix, suffix)
        return max_so_far