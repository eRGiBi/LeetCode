class Solution:
    def isPalindrome(s: str) -> bool:

        s = s.replace(" ", "")

        j = len(s) - 1
        i = 0

        while i <= j:
            left = s[i]
            right = s[j]

            print(left, right)

            if not left.isalnum():
                i += 1

            elif not right.isalnum():
                j -= 1

            elif left.lower() != right.lower():
                return False

            else:
                i += 1
                j -= 1

        return True


if __name__ == '__main__':
    print(Solution.isPalindrome("a.b,."))
