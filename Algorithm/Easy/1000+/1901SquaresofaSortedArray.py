#!/user/bin/env python
# -*- coding: utf-8 -*-
# @File : 1901SquaresofaSortedArray.py
# @Author : Martin Yan
# @Time : 2021/4/21 下午8:19
# @Software : PyCharm

class Solution:
    """
    @param A: The array A.
    @return: The array of the squares.
    """
    def SquareArray(self, A):
        # write your code here
        for i in range(len(A)):
            A[i] = A[i] * A[i]
        A.sort()
        return A