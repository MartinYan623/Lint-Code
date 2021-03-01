import copy


class Solution:
    """
    @param n: An integer.
    @return: A string list.
    """

    def printX(self, n):
        # write your code here.
        result = []
        subresult = []
        if n == 1:
            return ['X']
        for i in range(int(n / 2)):
            subresult.append(' ' * i + 'X' + ' ' * (n - 2 * i - 2) + 'X' + ' ' * i)

        result = copy.deepcopy(subresult)

        if n % 2 != 0:
            result.append(' ' * int((n - 1) / 2) + 'X' + ' ' * int((n - 1) / 2))

        for j in range(len(subresult) - 1, -1, -1):
            result.append(subresult[j])

        return result
