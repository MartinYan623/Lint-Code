class Solution:
    """
    @param n: The guest paid
    @param m: the price
    @return: the sum of the number of banknotes
    """
    def coinProblem(self, n, m):
        # Write your code here
        back=n-m
        count=0
        list=[100, 50, 20, 10, 5, 2, 1]
        for i in range (len(list)):
            while back>=list[i]:
                count+=1
                back=back-list[i]
                if back==0:
                    return count