def longestCommonPrefix(self, strs: List[str]) -> str:
    ans = ""
    v = sorted(strs)
    first = v[0]
    last = v[-1]
    for i in range(min(len(first), len(last))):
        if (first[i] != last[i]):
            return ans
        ans += first[i]
    return ans


def longestCommonPrefix2(self, strs: List[str]) -> str:

    res = ""
    smallest_len = len(strs[0])

    if smallest_len == 1:
        return strs[0]

    for strng in strs:
        if len(strng) < smallest_len:
            smallest_len = len(strng)

    for i in range(len(strs) - 1):

        c = strs[0][i]

        for j in range(len(strs) - 1):
            print(j)
            if strs[j][i] != c:
                break
        else:
            res += c
    return res

