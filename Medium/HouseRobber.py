class Solution:
    def rob(self, nums: List[int]) -> int:

        opt = [0] * (len(nums) + 1)
        opt[1] = nums[0]
        for n in range(1, len(nums)):
            opt[n + 1] = max(opt[n], nums[n] + opt[n - 1])
        return opt[-1]