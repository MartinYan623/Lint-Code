class Solution:
    """
    @param a: A number
    @return: Returns the maximum number after insertion
    """

    def InsertFive(self, a):
        # write your code here
        if a == 0: return 50
        origin_a = a
        number = []
        count = 0
        a = abs(a)
        while a:
            count += 1
            b = a % 10
            a = a // 10
            number.append(b)
        number.reverse()
        result = 0
        flag = 0
        # 判断原始a是正数还是负数
        if origin_a > 0:
            for i in range(count):
                if number[i] <= 5 and flag == 0:
                    result += 5 * pow(10, count - i)
                    flag = 1
                result += number[i] * pow(10, count - i - flag)
            return result
        else:
            for i in range(count):
                if number[i] >= 5 and flag == 0:
                    result += 5 * pow(10, count - i)
                    flag = 1
                result += number[i] * pow(10, count - i - flag)
            return result * -1
