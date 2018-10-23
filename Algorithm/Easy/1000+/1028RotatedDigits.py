class Solution:
    """
    @param N: a positive number
    @return: how many numbers X from 1 to N are good
    """
    def rotatedDigits(self, N):
        # write your code here
        answer=0
        for i in range(1,N+1):
            flag=True
            count=0
            num=i
            while i !=0:
                if i % 10 == 3 or i % 10 == 4 or i % 10 == 7:
                    flag=False
                if i % 10 == 0 or i % 10 == 1 or i % 10 == 8:
                    count+=1
                i = i // 10
            if flag==True and count!=len(str(num)):
                answer+=1
        return answer
