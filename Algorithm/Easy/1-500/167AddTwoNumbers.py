"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    """
    @param l1: the first list
    @param l2: the second list
    @return: the sum list of l1 and l2
    """

    def addLists(self, l1, l2):
        # write your code here
        if l1 is None: return l2
        if l2 is None: return l1

        h1 = l1
        h2 = l2
        # 只有两个链表的下一个节点数都为None,退出循环
        while h1.next is not None or h2.next is not None:
            # 若只有一条链表的下一个节点为None，补充为0,不影响后续的加法结果
            if h1.next == None: h1.next = ListNode(0)
            if h2.next == None: h2.next = ListNode(0)
            h1.val = h1.val + h2.val
            # 当加结果>=10,当前结果节点为个位数，下一个节点+1
            if h1.val >= 10:
                h1.val = h1.val % 10
                h1.next.val += 1
            h1 = h1.next
            h2 = h2.next
        else:
            h1.val = h1.val + h2.val
            # 链表尾部的计算，如果>=10，则在尾部再添加一个节点
            if h1.val >= 10:
                h1.val = h1.val % 10
                h1.next = ListNode(1)
        return l1
