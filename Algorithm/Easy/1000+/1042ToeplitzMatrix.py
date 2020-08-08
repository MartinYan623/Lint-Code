class Solution:
    """
    @param matrix: the given matrix
    @return: True if and only if the matrix is Toeplitz
    """
    def isToeplitzMatrix(self, matrix):
        # Write your code here
        col=len(matrix[0])
        row=len(matrix)
        for i in range(1, row):
            for j in range(1, col):
                if matrix[i][j] != matrix[i-1][j-1]:
                    return False
        return True