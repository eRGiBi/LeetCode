class Solution:
    def countTime(self, time: str) -> int:

        ans = 1

        if time[0] == '?' and time[1] == '?':
            ans *= 24
        elif time[0] == '?' and time[1] != '?':
            if time[1] >= '5':
                ans *= 2
            else:
                ans *= 3
        elif time[1] == '?':
            if time[0] == '2':
                ans *= 4
            else:
                ans *= 10

        if time[4] == '?':
            ans = ans * 10
        if time[3] == '?':
            ans = ans * 6

        return ans


class Solution2:
    def countTime(self, time: str) -> int:
        pattern = time.replace('?', '.')
        return sum(
            re.fullmatch(pattern, f'{hour:02}:{minute:02}') is not None
            for hour in range(24)
            for minute in range(60)
        )
