class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        counters = {}

        for i in range(len(nums)):

            if nums[i] not in counters.keys():
                counters[nums[i]] = 1

            counters[nums[i]] += 1

        srted = sorted(counters.keys(), key=lambda x: counters[x], reverse=True)

        res = []
        for i in range(k):
            res.append(srted[i])

        return res
