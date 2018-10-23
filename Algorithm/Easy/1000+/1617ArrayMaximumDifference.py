class Solution:
    """
    @param a: the array a
    @return: return the maximum value
    """

    def getAnswer(self, a):
        # Write your code here
        answer = 0
        for i in range(len(a)):
            for j in range(i, len(a)):
                if a[i] % 2 == 1 and a[j] % 2 == 0 and a[j] - a[i] > answer:
                    answer = a[j] - a[i]
        return answer



