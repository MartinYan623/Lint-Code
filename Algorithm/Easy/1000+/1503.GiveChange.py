#!/user/bin/env python
# -*- coding: utf-8 -*-
# @File : 1503.GiveChange.py
# @Author : Martin Yan
# @Time : 2021/4/21 下午8:22
# @Software : PyCharm

class Solution:
    """
    @param amount: The amount you should pay.
    @return: Return the minimum number of coins for change.
    """
    def giveChange(self, amount):
        # write you code here.
        change = 1024-amount
        number = 0
        while change>=64:
            change = change-64
            number +=1
        while change>=16:
            change = change-16
            number +=1
        while change>=4:
            change = change-4
            number +=1
        while change>=1:
            change = change-1
            number +=1
        return number