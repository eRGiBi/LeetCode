class Solution:
    def similarPairs(self, words: List[str]) -> int:

        c = 0
        for i, word in enumerate(words):
            words[i] = set([*word])

        for word in words:
            for target in words:
                if word == target:
                    c += 1
            c -= 1
        return c // 2

class Solution:
    def similarPairs(self, words: List[str]) -> int:

        c = 0
        for i, word in enumerate(words):
            words[i] = {*word}

        return len(set(words)) - len(words)