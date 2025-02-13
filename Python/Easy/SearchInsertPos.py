import bisect
from typing import List


def searchInsert(nums: List[int], target: int) -> int:
    low, high = 0, len(nums)

    while len(nums) != 1:

        mid = (low + high) // 2
        if target > nums[mid]:
            low = mid + 1
        else:
            high = mid
    return low


if __name__ == '__main__':
    print(searchInsert([1, 3, 5, 6, 7, 8, 9, 34, 634, 737], 634))
