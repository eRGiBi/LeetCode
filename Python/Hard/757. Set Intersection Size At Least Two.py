from typing import List


class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:

        min_pos = 2 * len(intervals)

        nums = []

        m = 0

        for interval in intervals:
            if interval[1] > m:
                m = interval[1]

        occ = dict.fromkeys(range(1, m + 1), 0)

        for key in occ:
            for interval in intervals:
                if interval[0] <= key <= interval[1]:
                    occ[key] += 1
        print(occ)
        sort_occ = dict(sorted(occ.items(), key=lambda x: x[1], reverse=True))
        print(sort_occ)

        for interval in intervals:
            c = 0
            for k, v in occ.items():
                if c == 2: break

                if interval[0] <= k <= interval[1] and k in nums:
                    c += 1
                    continue

                if interval[0] <= k <= interval[1] and c != 2 and k not in nums:
                    nums.append(k)
                    c += 1
                    continue

        print(nums)
        return len(nums)

class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])  # Sort intervals based on end points
        nums = []

        for interval in intervals:
            start, end = interval

            # Find the two largest numbers not already in nums
            largest_not_in_nums = max(x for x in range(end, start - 1, -1) if x not in nums)

            # Add the two largest numbers to nums
            nums.extend([largest_not_in_nums - 1, largest_not_in_nums])

        return len(nums)