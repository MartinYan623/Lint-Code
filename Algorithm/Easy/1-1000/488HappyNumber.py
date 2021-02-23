class Solution:
    """
    @param: n: An integer
    @return: true if this is a happy number or false
    """

    def isHappy(self, n):
        # write your code here
        array = [n]
        turn = 0
        while n != 1:
            l = list(str(n))
            length = len(l)
            n = 0
            for i in range(length):
                n += int(l[i]) ** 2
            for i in range(turn):
                if n == array[i]:
                    return False
            array.append(n)
            turn += 1
        return True
