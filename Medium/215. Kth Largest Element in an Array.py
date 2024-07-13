class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        ind = 0
        lar_nums = [float('-inf')] * k

        for num in nums:
            if num >= lar_nums[-1]:

                for kth in range(len(lar_nums)):
                    if lar_nums[kth] <= num:
                        lar_nums.insert(kth, num)
                        lar_nums.pop()
                        break

        return lar_nums[-1]


if __name__ == '__main__':
    sol = Solution()
    print(sol.findKthLargest([], 13377))