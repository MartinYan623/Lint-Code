class Solution:
    """
    @param head: the given linked list
    @return:  the weighted sum in reverse order
    """
    def weightedSumReverse(self, head):
        # write your code here
        count=0
        p=head
        while p:
            count+=1
            p=p.next
        answer=0
        while head:
            answer+=head.val*count
            head=head.next
            count-=1
        return answer