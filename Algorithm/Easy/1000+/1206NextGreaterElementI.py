class Solution:
    """
    @param nums1: an array
    @param nums2: an array
    @return:  find all the next greater numbers for nums1's elements in the corresponding places of nums2
    """
    def nextGreaterElement(self, nums1, nums2):
        # Write your code here
        for i in range(len(nums1)):
            index=nums2.index(nums1[i])
            flag=False
            for j in range(index+1,len(nums2)):
                if nums2[j]>nums1[i]:
                    flag=True
                    nums1[i]=nums2[j]
                    break
            if flag==False:
                nums1[i]=-1
        return nums1
