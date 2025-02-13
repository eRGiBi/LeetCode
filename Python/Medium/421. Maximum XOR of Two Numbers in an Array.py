
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:

        m = nums[0] ^ nums[0]

        for i in range(len(nums)):
            for j in range(len(nums)):
                c = nums[i] ^ nums[j]
                if c > m:
                    m = c

        return m


