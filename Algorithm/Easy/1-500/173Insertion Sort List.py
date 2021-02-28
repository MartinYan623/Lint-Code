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
    @return: The head of linked list.
    """

    def insertionSortList(self, head):
        # write your code here
        """
        if head is None:
            return None
        if head.next is None:
            return head
        l=ListNode(-9999)
        while head:
            node=l
            fol=head.next
            while cur:
                if check.val<cur.val:
                    pre=cur
                    cur=cur.next
                else:
                    head=head.next
                    check.next=cur
                    pre.nect=check
                    break
            head=head.next
            pre.next=check
        return l.next
        """
        if head is None:
            return None
        if head.next is None:
            return head
        l = ListNode(-9999)
        while head:
            node = l
            fol = head.next
            while node.next and node.next.val < head.val:
                node = node.next
            head.next = node.next
            node.next = head
            head = fol
        return l.next
