class Solution:
    """
    @param nums: a list of integers
    @return: return a integer
    """
    def findShortestSubArray(self, nums):
        # write your code here
        dict={}
        # find the frequency of every number
        for i in range(len(nums)):
            if nums[i] not in dict.keys():
                dict[nums[i]]=1
            else:
                dict[nums[i]]+=1
        count=0
        frequent=[]
        # find the max_frequent number
        for k,v in dict.items():
            if v==count:
                frequent.append(k)
            if v>count:
                count=v
                frequent=[]
                frequent.append(k)
        frequent.append(count)
        # find the min_length number with max_frequent
        max_frequent=frequent[-1]
        min_length=50000
        for i in range(len(frequent)-1):
            value=frequent[i]
            count=0
            start=0
            for j in range(len(nums)):
                if nums[j]==value:
                    if count==0:
                        start=j
                    count+=1
                    if count==max_frequent and min_length>(j-start+1):
                        min_length=j-start+1
        return min_length