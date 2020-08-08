class Solution:
    """
    @param funds: The investment each time
    @param a: The initial funds of A
    @param b: The initial funds of B
    @param c: The initial funds of C
    @return: The final funds
    """
    def getAns(self, funds, a, b, c):
        # Write your code here
        times=len(funds)
        for i in range(times):
            if a<=b:
                if a<=c:
                    a+=funds[i]
                else:
                    c+=funds[i]
            elif b<=c:
                b+=funds[i]
            else:
                c+=funds[i]
        return[a,b,c]