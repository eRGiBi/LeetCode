from collections import Counter


def longestPalindrome(s: str) -> int:

    c = Counter(s)
    num = 0
    odd = 0

    for val in c.values():
        if val % 2 == 0:
            num += val
        else:
            odd = 1
            num += val - 1

    return num + odd

def longestPalindromeHash(self, s: str) -> int:

        count = {}
        ans = []
        odd = 0
        for word in s:
            if word not in count:
                count[word] = 1
            else:
                count[word] += 1
        for times in count.values():
            ans.append(times)
            if times % 2 != 0:
                odd += 1
        if odd != 0:
            return sum(ans) - odd + 1
        elif odd == 0:
            return sum(ans) - odd


if __name__ == '__main__':
    print(longestPalindrome("abccccdd"))