class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        nums = []

        nums.append([1])

        for i in range(numRows - 1):
            newRow = [1]

            for j in range(i):
                newRow.append(nums[i][j] + nums[i][j + 1])

            newRow.append(1)
            nums.append(newRow)

        return nums