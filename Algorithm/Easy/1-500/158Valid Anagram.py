class Solution:
    """
    @param s: The first string
    @param b: The second string
    @return true or false
    """

    def anagram(self, s, t):
        # write your code here
        l1 = list(s)
        l2 = list(t)
        length1 = len(l1)
        length2 = len(l2)
        if length1 != length2:
            return False
        else:
            for i in range(length1):
                for j in range(length2):
                    fg = False
                    if l1[i] == l2[j]:
                        l1[i] = 0
                        l2[j] = 0
                        fg = True
                        break
                if fg == False:
                    return False
            return True
