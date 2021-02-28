"""
Definition of ListNode
"""

class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next



class Solution:
    """
    @param: head: The first node of linked list
    @param: x: An integer
    @return: A ListNode
    """

    def partition(self, head, x):
        # write your code here
        if head is None:
            return head
            # 新建两个节点
        first = ListNode(-1)
        second = ListNode(-1)
        cur1, cur2 = first, second
        # 遍历原始链表
        while head:
            if head.val < x:
                cur1.next = head
                head = head.next
                cur1 = cur1.next
            else:
                cur2.next = head
                head = head.next
                cur2 = cur2.next
                # 合并
        cur1.next = second.next
        cur2.next = None
        return first.next
