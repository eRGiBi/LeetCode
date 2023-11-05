class Solution:
    def findTargetSumWays(self, nums: List[int], target: int, s=0, i=0, memo=None) -> int:

        if memo is None:
            memo = {}

        if (i, s) in memo:
            return memo[(i, s)]

        num_of_exp = 0

        if len(nums) == i:
            if target == s:
                num_of_exp += 1

        else:
            num_of_exp += self.findTargetSumWays(nums, target, s + nums[i], i + 1)
            num_of_exp += self.findTargetSumWays(nums, target, s - nums[i], i + 1)

        memo[(i, s)] = num_of_exp
        return memo[(i, s)]


class Solution2:
    def findTargetSumWays(self, nums, target):
        total_sum = sum(nums)
        if abs(target) > total_sum or (total_sum + target) % 2 != 0:
            return 0

        target_sum = (total_sum + target) // 2
        dp = [0] * (target_sum + 1)
        dp[0] = 1

        for num in nums:
            print(num + ":")
            for i in range(target_sum, num - 1, -1):
                print('\t' + i)
                dp[i] += dp[i - num]

        return dp[target_sum]