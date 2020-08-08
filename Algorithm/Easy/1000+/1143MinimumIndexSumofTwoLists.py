import copy
class Solution:
    """
    @param list1: a list of strings
    @param list2: a list of strings
    @return: the common interest with the least list index sum
    """
    def findRestaurant(self, list1, list2):
        # Write your code here
        copy_list1=list1.copy()
        answer=[]
        for i in range(len(list1)):
            flag=False
            for j in range(len(list2)):
                if list1[i]==list2[j]:
                    flag=True
                    list1[i]=i+j
            if flag==False:
                list1[i]=2000
        min_sum=min(list1)
        for i in range(len(list1)):
            if list1[i]==min_sum:
                answer.append(copy_list1[i])
        return answer
