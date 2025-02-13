class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        if s == "":
            return True
        i = 0
        for t_s in t:
            if t_s == s[i]:
                if len(s) == i + 1:
                    return True
                i += 1

        return False

