import heapq


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

class Solution2:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = nums[:k]
        heapq.heapify(heap)

        for num in nums[k:]:
            if num > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, num)

        return heap[0]


if __name__ == '__main__':
    sol = Solution()
    print(sol.findKthLargest([], 13377))