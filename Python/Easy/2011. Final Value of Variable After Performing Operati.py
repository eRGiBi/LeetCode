class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:

        x = 0

        for op in operations:
            if op == "++X" or op == "X++":
                x += 1
            else:
                x -= 1
        return x


class Solution2:
    def finalValueAfterOperations(self, operations: List[str]) -> int:

       x = 0
       for op in operations:
           x += 44 - ord(op[1])
       return x

class Solution3:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        op_dict = {"--X": -1, "X--": -1,
                   "++X": 1, "X++": 1}
        return sum(op_dict[op] for op in operations)