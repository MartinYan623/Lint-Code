"""
Definition for singly-linked list.
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    """
    @param: head: a ListNode
    @return: a ListNode
    """

    def swapPairs(self, head):
        # write your code here
        if head is None or head.next is None:
            return head
        p = ListNode(0)
        p.next = head
        head = p
        q = head.next
        k = q.next
        while k:
            q.next = k.next
            k.next = q
            p.next = k
            p = q
            if q.next is None:
                q = None
                k = None
            else:
                q = q.next
                k = q.next
        head = head.next
        return head
