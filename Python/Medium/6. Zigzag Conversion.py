class Solution:
    def convert(self, s: str, numRows: int) -> str:

        if numRows == 1 or numRows > len(s):
            return s

        i = 0
        m = [[None for _ in range(len(s))] for _ in range(numRows)]
        cur_col = 0

        while i + 1 < len(s):

            for d in range(min(numRows - 1, len(s) - i - 1)):
                m[d][cur_col] = s[i]
                i += 1

            # i -= 1

            for diag in range(min(numRows - 1, len(s) - i - 1)):
                print("diag")
                print(numRows - diag - 1, cur_col, s[i])
                m[numRows - diag - 1][cur_col] = s[i]
                cur_col += 1
                i += 1
        else:
            print(d + 1, cur_col, s[i])
            m[d + 1][cur_col] = s[i]

        print(m)
        ans = ""
        for row in m:
            for l in row:
                if l is not None:
                    ans += l

        return ans


if numRows == 1 or numRows >= len(s):
            return s

        i = 0
        m = [[] for _ in range(numRows)]

        while i +  1 < len(s):

            for d in range(min(numRows, len(s) - i - 1)):
                m[d].append(s[i])
                i += 1
            for diag in range(numRows - 2, 0, -1):
                if i == len(s):
                    break
                print("diag", diag, s[i])
                m[diag].append(s[i])
                i += 1

        for i in range(numRows):
            m[i] = ''.join(m[i])

        return ''.join(m)




if __name__ == '__main__':
    s = Solution()
    print(s.convert("PAYPALISHIRING", 3))