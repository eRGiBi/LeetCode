class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True

        for i in range((num // 2) + 1):
            if i * i == num:
                return True
        return False

class Solution2:
    def isPerfectSquare(self, num: int) -> bool:

        if num == 1:
            return True

        for i in range(num // 2):
            if num / (i + 1) == i+1:
                return True
        return False


class Solution3:
    def isPerfectSquare(self, num: int) -> bool:

        if num == 1:
            return True

        i = 1
        while num > 0:
            num -= i
            i += 2

        return num == 0


class Solution4:
    def isPerfectSquare(self, num: int) -> bool:

        if num == 1:
            return True

        low = 0
        mid = num // 2
        high = num

        while low <= high:

            mid = (high + low) // 2
            sq = mid ** 2

            if sq == num:
                return True
            elif sq > num:
                high = mid - 1
            else:
                low = mid + 1

        return False