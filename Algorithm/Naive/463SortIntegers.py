class Solution:
    """
    @param: A: an integer array
    @return:
    """

    def sortIntegers(self, A):
        # write your code here
        length = len(A)
        while length > 0:
            for i in range(0, length - 1):
                if A[i] > A[i + 1]:
                    temp = A[i]
                    A[i] = A[i + 1]
                    A[i + 1] = temp
            length -= 1

# This is a question about sort