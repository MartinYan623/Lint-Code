import math
"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    """
    @param head: the head of linked list.
    @return: a middle node of the linked list
    """

    def middleNode(self, head):
        # write your code here
        if head is None or head.next is None:
            return head
        count = 1
        p = head.next
        while p:
            count += 1
            p = p.next
        if math.floor((int(count) + 1) / 2) == 1:
            return head
        else:
            q = head.next
            for i in range(1, math.floor((int(count) + 1) / 2) - 1):
                q = q.next
            return q
