class Solution:
    """
    @param A: an array
    @param B: an array
    @return: dot product of two array
    """
    def dotProduct(self, A, B):
        # Write your code here
        if len(A)!=len(B) or len(A)==0 or len(B)==0:
            return -1
        else:
            sum=0
            for i in range(len(B)):
                sum+=A[i]*B[i]
            return sum