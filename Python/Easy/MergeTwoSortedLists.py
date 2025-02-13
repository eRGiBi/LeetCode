# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        merged_list = head = ListNode()

        while list1 and list2:

            if list1.val < list2.val:
                merged_list.next = list1

                merged_list, list1 = merged_list.next, list1.next;

            else:
                merged_list.next = list2

                list2, merged_list = list2.next, list2

        if list1 or list2:
            merged_list.next = list1 if list1 else list2

        return head.next
