class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        if p == '': return False

        if s == p: return True

        if s == '' or p == '*': return True

        if p[0] == '?':
            return self.isMatch(s[1::], p[1::])

        if p[0] == '*':

            for i in range(len(s) - 1):
                if s[i] == p[1]:
                    return self.isMatch(s[i + 1::], p[1::])
            else:
                return False

        if s[0] == p[0]:
            return self.isMatch(s[1::], p[1::])
