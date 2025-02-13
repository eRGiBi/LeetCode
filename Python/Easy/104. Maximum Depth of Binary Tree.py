# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        depth = 0

        def rec(root, cur_depth):
            if root == None:
                return cur_depth

            return max(rec(root.left, cur_depth + 1), rec(root.right, cur_depth + 1))

        return rec(root, 0)


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        depth = 0

        def rec(root):
            if not root:
                return 0

            return max(rec(root.left), rec(root.right)) + 1

        return rec(root)