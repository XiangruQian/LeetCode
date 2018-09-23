# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l3 = ListNode(0)
        head = l3
        while l1 is not None and l2 is not None:
            l3.next = ListNode(int((l3.val + l1.val + l2.val) / 10))
            l3.val = (l3.val + l1.val + l2.val) % 10
            l3 = l3.next
            l1 = l1.next
            l2 = l2.next
        while l1 is not None:
            l3.next = ListNode(int((l3.val + l1.val)/ 10))
            l3.val = (l3.val + l1.val) % 10
            l3 = l3.next
            l1 = l1.next
        while l2 is not None:
            l3.next = ListNode(int((l3.val + l2.val) / 10))
            l3.val = (l3.val + l2.val) % 10
            l3 = l3.next
            l2 = l2.next
        if l3.val >= 10:
            l3.next = ListNode(int(l3.val / 10))
            l3.val = l3.val % 10
        tmp = head
        while tmp.next is not None:
            if tmp.next.next is None and tmp.next.val == 0:
                tmp.next = None
                return head
            tmp = tmp.next
        return head


l1 = ListNode(0)
l2 = ListNode(0)

a = Solution()
x = a.addTwoNumbers(l1, l2)
while x is not None:
    print(x.val)
    x = x.next