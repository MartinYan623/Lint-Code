class Solution:
    """
    @param: str: A string
    @return: a boolean
    """

    def isUnique(self, str):
        # write your code here
        array = list(str)
        result = {}
        for i in range(len(str)):
            if array[i] not in result.keys():
                result[array[i]] = 1
            else:
                return False
        return True


class Solution:
    """
    @param: str: A string
    @return: a boolean
    """

    def isUnique(self, str):
        # write your code here
        array = list(str)
        length = len(array)
        fg = True
        ans = 0
        for i in range(length - 1):
            for j in range(i + 1, length):
                ans = ord(array[i]) ^ ord(array[j])
                if ans == 0:
                    fg = False
                    break
        if fg:
            return True
        else:
            return False
