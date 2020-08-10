class Solution:
    """
    @param A: A string
    @param B: A string
    @return: if string A contains all of the characters in B return true else return false
    """

    def compareStrings(self, A, B):
        # write your code here
        dict_a = {}
        dict_b = {}
        if B == "":
            return True
        if A == "":
            return False
        for i in A:
            if i not in dict_a:
                dict_a[i] = 1
            else:
                dict_a[i] += 1
        for i in B:
            if i not in dict_b:
                dict_b[i] = 1
            else:
                dict_b[i] += 1
        for k, v in dict_b.items():
            if k not in dict_a.keys() or v > dict_a[k]:
                return False
        return True
