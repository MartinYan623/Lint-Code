class Solution:
    """
    @param matrix: matrix, a list of lists of integers
    @param target: An integer
    @return: a boolean, indicate whether matrix contains target
    """

    def searchMatrix(self, matrix, target):
        # write your code here
        m = len(matrix)
        n = len(matrix[0])
        mm = 0
        if target < matrix[0][0]:
            return False
        for i in range(m):
            print(i)
            if target >= matrix[i][0] and target <= matrix[i][n - 1]:
                mm = i
                break
        for j in range(n):
            if target == matrix[mm][j]:
                return True
        return False

# First search the element by row to know which row includes it
# And then search the element by column one by one
# Time complexity is O(m)+O(n)
# If you want to reduce the time complexity to O(log(m)+log(n)), you need to use binary search
