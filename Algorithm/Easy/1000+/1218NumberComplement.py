class Solution:
    """
    @param num: an integer
    @return: the complement number
    """
    def findComplement(self, num):
        # Write your code here
        bit=[]
        while num:
            if num % 2 ==1:
                bit.append(0)
            else:
                bit.append(1)
            num=num>>1
        answer=0
        for i in range(len(bit)):
            answer+=bit[i]*pow(2,i)
        return answer