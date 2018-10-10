class Solution:
    """
    @param points: List[List[int]]
    @return: return a double
    """
    def largestTriangleArea(self, points):
        # write your code here
        n = len(points)
        max_area = 0
        def area(points, i, j, k):
            x = (points[i][0] - points[j][0], points[i][1] - points[j][1])
            y = (points[i][0] - points[k][0], points[i][1] - points[k][1])
            return 0.5 * abs(x[0]*y[1] - x[1]*y[0])
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    max_area = max(max_area, area(points, i, j, k))
        return max_area