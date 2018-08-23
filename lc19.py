class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        size = 0
        p = head
        while p is not None:
            p = p.next
            size += 1
        if size == n:
            return head.next
        p = head
        for _ in range(size - n - 1):
            p = p.next
        if p.next is not None:
            p.next = p.next.next
        return head


l = ListNode(1)
a = Solution()
l = a.removeNthFromEnd(l, 1)
print(l)