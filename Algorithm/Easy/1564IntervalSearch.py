class Solution:
    """
    @param intervalList:
    @param number:
    @return: return True or False
    """
    def isInterval(self, intervalList, number):
        # Write your code here
        length=len(intervalList)
        for i in range(length):
            if number>=intervalList[i][0] and number<=intervalList[i][1]:
                return "True"
        return "False"