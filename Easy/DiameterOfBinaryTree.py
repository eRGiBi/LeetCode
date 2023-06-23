class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxd = 0

        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            self.maxd = max(self.maxd, left + right)
            return max(left, right) + 1

        dfs(root)
        return self.maxd


def diameterOfBinaryTreeW(root: Optional[TreeNode]) -> int:
    start = root
    end1 = 0
    end1_steps = 0
    end2 = 0
    end2_steps = 0

    while not root.left or not root.right:
        if not root.left:
            start = root.left
        else:
            start = root.right

    while not start.left and not start.right:

        if start.left:
            end1 = start.left
            end1_steps += 1
        elif start.right:
            end1 = start.right
            end1_steps += 1

    while not start.left and not start.right:

        if start.left:
            end2 = start.left
            end2_steps += 1
        elif start.right:
            end2 = start.right
            end2_steps += 1

    return end1_steps + end2_steps
