from typing import List


class Solution:
    @staticmethod
    def removeElement(nums: List[int], val: int) -> int:

        k = 0

        if len(nums) == 0:
            return 0

        for x in range(len(nums)):
            if nums[x] == val:
                nums[x] = 51
                k += 1

        index = 0
        for i in nums:
            if nums[i] == 51:
                continue
            else:
                nums[index] = nums[i]
                index += 1

        return k

    asd = removeElement(([0, 1, 2, 2, 3, 0, 4, 2]), 2)
    print(asd)
