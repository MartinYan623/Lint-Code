"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    """
    @param: head: the first node of linked list.
    @return: An integer
    """
    def countNodes(self, head):
        # write your code here
        count=0
        cur=head
        while cur:
            count+=1
            cur=cur.next
        return count