class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        def backtrack(sol, tl):
            if len(tl) == len(nums):
                sol.append(tl[:])
            else:
                for j in range(len(nums)):
                    if used[j] or j > 0 and nums[j] == nums[j - 1] and used[j - 1]:
                        continue
                    else:
                        tl.append(nums[j])
                        used[j] = True
                        backtrack(sol, tl)

                        used[j] = False
                        if len(tl) != 0:
                            tl.pop()

        nums.sort()
        sol = []
        tl = []
        used = [False] * len(nums)

        backtrack(sol, tl)

        return sol

class Solution2:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        for n in nums:
            new_ans = []
            for lst in ans:
                for i in range(len(lst) + 1):
                    new_ans.append(lst[:i] + [n] + lst[i:])
                    if i < len(lst) and lst[i] == n:
                        break
                ans = new_ans
        return ans