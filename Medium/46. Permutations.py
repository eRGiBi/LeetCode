class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        def backtrack(sol, tl):

            if len(tl) != len(nums):
                for num in nums:
                    if num not in tl:
                        tl.append(num)
                        backtrack(sol, tl)
            else:
                sol.append(tl[:])
            if len(tl) > 0:
                tl.pop()

        sol = []
        temp_list = []

        backtrack(sol, temp_list)

        return sol

class Solution2:
    class Solution:
        def permute(self, nums: List[int]) -> List[List[int]]:

            def backtrack(start):
                if start == len(nums):
                    sol.append(nums[:])
                    return
                for i in range(start, len(nums)):
                    nums[start], nums[i] = nums[i], nums[start]  # Swap elements
                    backtrack(start + 1)
                    nums[start], nums[i] = nums[i], nums[start]  # Restore the original order

        sol = []
        backtrack(0)
        return sol