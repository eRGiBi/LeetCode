from typing import List


# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
#
# You must implement a solution with a linear runtime complexity and use only constant extra space.

def singleNumber(self, nums: List[int]) -> int:
    if len(nums) == 1:
        return nums[0]

# class Solution {
#     public int singleNumber(int[] nums) {
#         int ans = 0;
#         for (int i = 0; i < nums.length ; i++ ){
#             ans ^= nums[i];
#         }
#         return ans;
#     }
# }

if __name__ == "__main__":
    print(singleNumber([4, 1, 2, 1, 2]))
