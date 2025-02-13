class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        x = len(nums)
        for i in range (x):
            for j in range (x):
                if (i != j) and ((nums[i] + nums[j])  == target):
                    OutList = []
                    OutList.append(i)
                    OutList.append(j)

                    return OutList
                    break