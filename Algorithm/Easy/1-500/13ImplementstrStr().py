class Solution:
    """
    @param: source: source string to be scanned.
    @param: target: target string containing the sequence of characters to match
    @return: a index to the first occurrence of target in source, or -1  if target is not part of source.
    """

    def strStr(self, source, target):
        # write your code here

        if source is None or target is None:
            return -1
        else:
            checkString_1 = list(source)
            checkString_2 = list(target)
            i = len(source)
            j = len(target)
            m = 0
            n = 0
            if j == 0:
                return 0
            elif i == 0 and j != 0:
                return -1
            else:
                if j == 1:
                    while m < i:
                        if checkString_1[m] == checkString_2[0]:
                            return m
                            break
                        m = m + 1
                else:
                    while m < i and n < j:
                        if checkString_1[m] == checkString_2[n]:
                            n = n + 1
                        m = m + 1
                    if n == j:
                        return m - n
                    else:
                        return -1
