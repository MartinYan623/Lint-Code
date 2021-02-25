class Solution:
    """
    @param: A: sorted integer array A
    @param: B: sorted integer array B
    @return: A new sorted integer array
    """

    def mergeSortedArray(self, A, B):
        # write your code here
        if A is None:
            return B
        if B is None:
            return A
        l = []
        a = 0
        b = 0
        alength = len(A)
        blength = len(B)
        while a < alength and b < blength:
            if A[a] <= B[b]:
                l.append(A[a])
                a += 1
            else:
                l.append(B[b])
                b += 1
        if a != alength:
            for i in range(a, alength):
                l.append(A[i])
        if b != blength:
            for i in range(b, blength):
                l.append(B[i])
        return l
