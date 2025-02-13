from collections import Counter


def majorityElement(nums: List[int]) -> int:

    dic = {}
    for n in nums:
        if dic.__contains__(n):
            dic[n] += 1
        else:
            dic[n] = 1
        if dic[n] > len(nums) // 2:
            return n

def majorityElement2(self, nums: List[int]) -> int:

    current = nums[0]
    count = 0

    for i in range(len(nums)):

        if count == 0: current = nums[i]

        count += 1 if current == nums[i] else -1

    return current
if __name__ == '__main__':
    majorityElement([2, 2, 1, 1, 1, 2, 2])
