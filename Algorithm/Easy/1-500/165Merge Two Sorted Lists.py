"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    """
    @param: l1: ListNode l1 is the head of the linked list
    @param: l2: ListNode l2 is the head of the linked list
    @return: ListNode head of linked list
    """

    def mergeTwoLists(self, l1, l2):
        # write your code here
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        else:
            if l1.val <= l2.val:
                newhead = p = l1
                l1 = l1.next
            else:
                newhead = p = l2
                l2 = l2.next

            while l1 and l2:
                if l1.val <= l2.val:
                    p.next = l1
                    l1 = l1.next
                    p = p.next
                else:
                    p.next = l2
                    l2 = l2.next
                    p = p.next
            if l1:
                p.next = l1
            if l2:
                p.next = l2
        return newhead
