class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:

        if len(nums) == 0:
            return []

        start = nums[0]
        res = []
        nums.append(0.5)

        for i in range(len(nums) - 1):

            if nums[i] != nums[i + 1] - 1:

                if start == nums[i]:
                    res.append(f"{nums[i]}")
                else:
                    res.append(f"{start}->{nums[i]}")

                start = nums[i + 1]

        return res