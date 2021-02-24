"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    """
    @param head: The first node of linked list.
    @param n: An integer
    @return: The head of linked list.
    """

    def removeNthFromEnd(self, head, n):
        # write your code here
        l1 = head
        count = 1
        # 找到最后一个结点
        while l1.next is not None:
            l1 = l1.next
            count += 1
        # 计算应该删除的第几个结点
        delete = count - n + 1
        # 处理删除头结点的情况
        if delete == 1:
            return head.next
        # 删除非头结点的情况
        l1 = head
        l2 = head
        while delete:
            if delete == 1:
                l1.next = l2.next
            else:
                l1 = l2
                l2 = l2.next
            delete -= 1
        # 最后返回head
        return head
