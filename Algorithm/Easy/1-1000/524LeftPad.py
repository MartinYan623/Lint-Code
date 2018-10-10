class StringUtils:
    """
    @param: originalStr: the string we want to append to
    @param: size: the target length of the string
    @param: padChar: the character to pad to the left side of the string
    @return: A string
    """
    @classmethod
    def leftPad(self, originalStr, size, padChar=' '):
        # write your code here
        if size<=len(originalStr):
            return originalStr
        else:
            diff=size-len(originalStr)
            l=""
            while diff>0:
                l=l+padChar
                diff-=1
            return l+originalStr

    @classmethod
    def leftPad(self, originalStr, size, padChar=' '):
        # write your code here
        if len(originalStr) >= size:
            return originalStr
        return (size - len(originalStr)) * padChar + originalStr