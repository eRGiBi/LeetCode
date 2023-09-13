class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        i = 1 if len(nums) > 0 else 0

        for n in nums:
            if n > nums[i - 1]:
                nums[i] = n
                i += 1

        return i

    def removeDuplicates2(self, nums: List[int]) -> int:
        x = 1
        for i in range(len(nums) - 1):
            if nums[i] != nums[i + 1]:
                nums[x] = nums[i + 1]
                x += 1
        return x
