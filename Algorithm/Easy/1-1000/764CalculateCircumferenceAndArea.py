import math
class Solution:
    """
    @param r: a Integer represent radius
    @return: the circle's circumference nums[0] and area nums[1]
    """
    def calculate(self, r):
        # write your code here
        return [float(2*round(math.pi,2)*r),float(round(math.pi,2)*math.pow(r,2))]