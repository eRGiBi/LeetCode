class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        def backtrack(ls, templs, nums, start):
            ls.append(templs[:])

            for i in range(start, len(nums)):

                templs.append(nums[i])
                backtrack(ls, templs, nums, i + 1)
                if len(templs) != 0:
                    templs.pop()

        ls = []
        templs = []
        start = 0

        backtrack(ls, templs, nums, 0)

        return ls

    def subsets2(self, nums: List[int]) -> List[List[int]]:

        def backtrack(start, tempList):
            result.append(tempList[:])
            for i in range(start, len(nums)):
                tempList.append(nums[i])
                backtrack(i + 1, tempList)
                tempList.pop()

        result = []
        nums.sort()
        backtrack(0, [])

        return result
