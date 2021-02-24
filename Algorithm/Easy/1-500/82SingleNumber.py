class Solution:
    """
    @param: A: An integer array
    @return: An integer
    """
    """
    def singleNumber(self, A):
        # write your code here
        length = len(A)
        for i in range(length):
            fg=True
            for j in range(length):
                if A[i]==A[j] and i!=j:
                    fg=False
                    break
            if fg:        
                return A[i]
    """

    def singleNumber(self, A):
        # write your code here
        length = len(A)
        ans = 0
        for i in range(length):
            ans ^= A[i]
        return ans
