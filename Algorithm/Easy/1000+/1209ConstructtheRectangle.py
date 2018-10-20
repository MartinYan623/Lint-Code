class Solution:
    """
    @param area: web pageâs area
    @return: the length L and the width W of the web page you designed in sequence
    """
    def constructRectangle(self, area):
        # Write your code here
        sqrt = int(pow(area,0.5))
        if area % sqrt == 0:
            return [sqrt,sqrt]
        else:
            for i in range(1,sqrt):
                if area % i ==0:
                    L = int(area / i)
                    W=i
            return [L,W]