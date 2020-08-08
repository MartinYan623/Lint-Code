class Solution:
    """
    @param n: count lucky numbers from 1 ~ n
    @return: the numbers of lucky number
    """
    def luckyNumber(self, n):
        # Write your code here
        count = 0
        for i in range(n):
            if '8' in str(i):
                count +=1
        return count

class Solution:
    """
    @param n: count lucky numbers from 1 ~ n
    @return: the numbers of lucky number
    """
    def luckyNumber(self, n):
        # Write your code here
        count=0
        for i in range(n+1):
            while i //10 !=0:
                num=i%10
                if num==8:
                    count+=1
                    break
                i=i//10
            if i == 8 :
                count+=1
        return count