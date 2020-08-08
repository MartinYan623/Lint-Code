class Solution:
    """
    @param grid: a 2D array
    @return: the perimeter of the island
    """
    def islandPerimeter(self, grid):
        # Write your code here
        row=len(grid)
        col=len(grid[0])
        answer=0
        for i in range(row):
            for j in range(col):
                if grid[i][j]==1:
                    sub_answer=4
                    if i-1>=0 and grid[i-1][j]==1:
                        sub_answer-=1
                    if j-1>=0 and grid[i][j-1]==1:
                        sub_answer-=1
                    if i+1 <= row-1 and grid[i+1][j]==1:
                        sub_answer-=1
                    if j+1 <= col-1 and grid[i][j+1]==1:
                        sub_answer-=1
                    answer+=sub_answer
        return answer