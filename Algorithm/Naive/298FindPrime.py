import math


class Solution:
    """
    @param n: an integer
    @return: return all prime numbers within n.
    """

    def prime(self, n):
        # write your code here
        if n == 1:
            return []
        result = [2]
        for num in range(3, n + 1):
            flag = True
            for i in range(2, int(math.sqrt(num)) + 1):
                if num % i == 0:
                    flag = False
                    break
            if flag:
                result.append(num)
        return result
