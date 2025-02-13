class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return

        # Initialize two pointers
        left, right = 0, 0

        while right < len(nums):
            if nums[right] != 0:
                # Swap non-zero element with the left pointer
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            right += 1