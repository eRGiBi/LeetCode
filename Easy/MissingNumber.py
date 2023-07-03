class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        s = 0
        for i in range(len(nums) + 1):
            s += i

        return s - sum(nums)

    def missingNumber2(self, nums: List[int]) -> int:

        res = len(nums)

        for i in nums:
            res ^= i
            res ^= nums[i]

        return res
