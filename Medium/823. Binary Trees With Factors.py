class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:

        res = []
        for x in range(len(arr)):
            for i in range(len(arr)):
                for j in range(len(arr)):

                    if i * k == x:
                        res.append(x, i, j)

        for i in range(len(arr)):
            if any(arr[i] * x for x in arr) == 0:
                res.append(arr[i])
                for j in range(len(arr)):

        return len(res)