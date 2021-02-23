class Solution:
    """
    @param: dictionary: an array of strings
    @return: an arraylist of strings
    """

    def longestWords(self, dictionary):
        # write your code here
        """
        length=len(dictionary)
        maxlength=0
        for i in range(length):
            a=len(dictionary[i])
            if a>maxlength:
                maxlength=a
        ans=[]
        for i in range(length):
             b=len(dictionary[i])
             if b==maxlength:
                ans.append(dictionary[i])
        return ans
        """
        length = len(dictionary)
        maxlength = 0
        ans = []
        for i in range(length):
            a = len(dictionary[i])
            if a > maxlength:
                maxlength = a
                del ans[:]
                ans.append(dictionary[i])
            elif a == maxlength:
                ans.append(dictionary[i])
        return ans
