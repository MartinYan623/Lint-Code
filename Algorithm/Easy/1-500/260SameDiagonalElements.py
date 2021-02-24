class Solution:
    """
    @param matrix: a matrix
    @return: return true if same.
    """

    def judgeSame(self, matrix):
        # write your code here.
        n = len(matrix)
        flag = True
        for i in range(n - 1):
            row = 1
            col = i + 1
            while col < n:
                if matrix[0][i] != matrix[row][col]:
                    flag = False
                    break
                row += 1
                col += 1
        return flag
