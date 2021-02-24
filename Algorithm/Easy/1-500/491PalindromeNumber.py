class Solution:
    """
    @param: num: a positive number
    @return: true if it's a palindrome or false
    """

    def isPalindrome(self, num):
        # write your code here
        string = str(num)
        l = list(string)
        length = len(l)
        i = 1
        while i < length / 2 + 1:
            if l[i - 1] != l[-i]:
                return False
            i += 1
        return True
