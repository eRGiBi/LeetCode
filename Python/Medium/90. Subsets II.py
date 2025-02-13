class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        def backtrack(sol, nums, temp_list, start):

            sol.append(temp_list[:])
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                temp_list.append(nums[i])
                backtrack(sol, nums, temp_list, i + 1)
                temp_list.pop()

        sol = []
        temp_list = []
        start = 0
        nums.sort()

        backtrack(sol, nums, temp_list, start)

        return sol
