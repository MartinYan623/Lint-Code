class Solution:
    """
    @param s: the given string
    @return: if a permutation of the string could form a palindrome
    """
    def canPermutePalindrome(self, s):
        # write your code here
        dict={}
        for i in range(len(s)):
            if s[i] not in dict:
                dict[s[i]]=1
            else:
                dict[s[i]]+=1
        count=0
        for k,v in dict.items():
            if v %2 ==1:
                count+=1
        if count<=1:
            return True
        else:
            return False