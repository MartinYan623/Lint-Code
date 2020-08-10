class Solution:
    """
    @param A: an integer sorted array
    @param target: an integer to be inserted
    @return: An integer
    """

    def searchInsert(self, A, target):
        # write your code here
        if A == [] or target <= A[0]:
            return 0
        for i in range(1, len(A)):
            if A[i] == target or A[i - 1] < target and target < A[i]:
                return i
            elif target > A[i] and i + 1 == len(A):
                return i + 1
