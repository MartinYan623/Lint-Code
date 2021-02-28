"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    """
    @param: head: The first node of linked list.
    @param: n: An integer
    @return: Nth to last node of a singly linked list.
    """

    def nthToLast(self, head, n):
        # write your code here
        if head is None or n == 0:
            return None
        count = 0
        pre = head
        while pre:
            count += 1
            pre = pre.next
        m = count - n
        while m:
            head = head.next
            m -= 1
        return head
