from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        maxSum = nums[0]
        currentSum = nums[0]

        for num in nums[1:]:
            currentSum = max(num, currentSum + num)
            maxSum = max(maxSum, currentSum)

        return maxSum

class Solution_Kadane:
    def maxSubArray(self, nums: List[int]) -> int:

        maxSum = -1E10
        c_sum = 0

        for i in range(len(nums)):
            c_sum += nums[i]
            maxSum = max(c_sum, maxSum)

            if c_sum < 0: c_sum = 0

        return maxSum