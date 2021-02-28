class Solution:
    """
    @param: A: A list of integers
    @param: elem: An integer
    @return: The new length after remove
    """

    def removeElement(self, A, elem):
        # write your code here
        length = len(A)
        i = 0
        while i < length:
            while A and A[i] == elem:
                del A[i]
                length -= 1
            i += 1
        ans = len(A)
        return ans
