from collections import Counter


class Solution:
    def canConstruct(ransomNote: str, magazine: str) -> bool:

        st1, st2 = Counter(ransomNote), Counter(magazine)

        if st1 == st2:
            return True
        return False

    def canConstruct2(a: str, b: str) -> bool:

        letter = [0 for _ in range(26)]

        for c in b:
            letter[ord(c) - 97] += 1

        for c in a:
            letter[ord(c) - 97] -= 1

        return not any((i < 0 for i in letter))

    def canConstruct3(self, ransomNote: str, magazine: str) -> bool:

        if len(magazine) < len(ransomNote):
            return False

        else:

            for ransomNote_char in set(ransomNote):

                if ransomNote.count(ransomNote_char) > magazine.count(ransomNote_char):
                    return False

            return True


if __name__ == '__main__':
    print(Solution.canConstruct("josh", "asdasd"))
