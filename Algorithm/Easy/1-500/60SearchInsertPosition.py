class Solution:
    """
    @param A: an integer sorted array
    @param target: an integer to be inserted
    @return: An integer
    """

    def searchInsert(self, A, target):
        # write your code here
        if A == [] or target <= A[0]:
            return 0
        for i in range(1, len(A)):
            if A[i] == target or A[i - 1] < target and target < A[i]:
                return i
            elif target > A[i] and i + 1 == len(A):
                return i + 1

    def searchInsert2(self, A, target):
        # write your code here
        if len(A) == 0:
            return 0
        for i, num in enumerate(A):
            if target <= num:
                return i
        return len(A)

    # 二分搜索方法
    def searchInsert3(self, A, target):
        left, right = 0, len(A) - 1  # 初始化左右端点位置
        while left <= right:  # 当条件合法时
            mid = left + (right - left) // 2  # 获取中点，如果是偶数取靠左的位置
            if A[mid] == target:  # 找到该数
                return mid  # 直接返回
            elif A[mid] > target:  # 如果当前位置数比插入值大
                right = mid - 1  # 更新右端点
            else:  # 如果当前位置数比插入值小
                left = mid + 1  # 更新左端点
        return left  # 返回插入位置，这里是左端位置
