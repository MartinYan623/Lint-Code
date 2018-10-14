class Solution:
    """
    @param num: the given number
    @return: The base 7 string representation
    """

    def convertToBase7(self, num):
        # Write your code here
        remainder = ""
        flag = True
        while num != 0:
            if num > 0:
                remainder += str(num % 7)
                num = int(num / 7)
            else:
                flag = False
                remainder += str((num % -7) * -1)
                num = int(num / 7)
        l = list(remainder)
        l.reverse()
        if not flag:
            return str(int("".join(l)) * -1)
        return "".join(l)
