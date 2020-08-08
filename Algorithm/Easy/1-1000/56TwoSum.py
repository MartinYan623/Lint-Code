# I used three different methods to fix this problem 
class Solution:
    """
    @param numbers: An array of Integer
    @param target: target = numbers[index1] + numbers[index2]
    @return: [index1, index2] (index1 < index2)

    def twoSum(self, numbers, target):
        # write your code here
        length=len(numbers)
        for i in range(length-1):
            for j in range(i+1,length):
                if numbers[i]+numbers[j]==target:
                    return [i,j]


    def twoSum(self, numbers, target):
        # write your code here
        for i,num in enumerate(numbers):
            sub_num=target-num
            if sub_num in numbers:
                sub_index=numbers.index(sub_num)
                if sub_index!=i:
                    #为真时的结果 if 判定条件 else 为假时的结果
                    return [i,sub_index] if sub_index>i else [sub_index,i]
    """

    def twoSum(self, numbers, target):
        # write your code here
        l = sorted(numbers)
        print(numbers)
        i = 0
        j = len(l) - 1
        while (i < j):
            if l[i] + l[j] == target:
                if l[i] == l[j]:
                    index1 = numbers.index(l[i])
                    index2 = numbers.index(l[j], index1 + 1, len(numbers))
                else:
                    index1 = numbers.index(l[i])
                    index2 = numbers.index(l[j])
                return [index1, index2] if index2 > index1 else [index2, index1]
            elif l[i] + l[j] < target:
                i += 1
            else:
                j -= 1