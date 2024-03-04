class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:

        res = 0

        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if nums[i] - nums[j] == k or nums[j] - nums[i] == k:
                    res += 1
        return res


