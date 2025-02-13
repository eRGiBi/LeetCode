class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:

        lst = []

        while head:
            lst.append(head)
            head = head.next

        size = len(lst)

        if size % 2 != 0:
            return lst[size // 2]
        else:
            return lst[(size // 2)]

