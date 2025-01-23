# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:

        nums = []
        while head:
            nums.append(head.val)
            head = head.next

        def sortedArrayToBST(nums):

            total_nums = len(nums)
            if not total_nums:
                return None

            mid = total_nums // 2

            return TreeNode(nums[mid], sortedArrayToBST(nums[:mid]), sortedArrayToBST(nums[mid + 1:]))

        return sortedArrayToBST(nums)