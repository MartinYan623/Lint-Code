class Solution:
    """
    @param: string: An array of Char
    @param: length: The true length of the string
    @return: The true length of new string
    """

    def replaceBlank(self, string, length):
        # write your code here
        if string is None: return None
        for char in string:
            if char == '':
                break
            if char != ' ':
                string += char
            else:
                string.append('%')
                string.append('2')
                string.append('0')
        for i in range(length):
            string.pop(0)
        return len(string)
