"""
Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
"""


class Solution:
    """
    @param: head: a ListNode
    @param: val: An integer
    @return: a ListNode
    """

    def removeElements(self, head, val):
        if head is None:
            return None
        # 可能链表中的所有元素val都等于val，所以需要新增一个头节点
        new = ListNode(0)
        new.next = head
        head = new
        pre = head
        # 遍历链表，删除等于val的所有节点
        while pre.next is not None:
            if pre.next.val == val:
                pre.next = pre.next.next
            else:
                pre = pre.next
        return new.next
