from typing import List


class Solution:
    def searchRange(nums: List[int], target: int) -> List[int]:

        pos = [-1, -1]

        fora = nums

        def search(nums: List[int], target: int) -> List[int]:

            if target == nums[(len(nums) / 2) + 1]:
                return (len(nums) / 2) + 1
            if target > nums[(len(nums) / 2) + 1]:
                for i in range(len(nums)/ 2):
                    nums.remove(i)
                search(nums, target)

        found = search(nums, target)
        i = 0
        while fora[found] != fora[i + found]:
            i -= 1
            pos[0] = fora[i+found]

        i=0
        while fora[found] != fora[i + found]:
            i += 1
            pos[1] = fora[i+found]