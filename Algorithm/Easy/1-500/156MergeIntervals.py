"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""


class Solution:
    """
    @param intervals: interval list.
    @return: A new interval list.
    """

    def merge(self, intervals):
        # write your code here
        if len(intervals) < 2:  # 数组长度小于2直接返回
            return intervals
        intervals = sorted(intervals, key=lambda x: x.start)  # 排序
        res = [intervals[0]]
        i = 1
        k = 0
        while i < len(intervals):
            if res[k].end >= intervals[i].start:  # 判断是否可以合并
                res[k] = Interval(res[k].start, res[k].end if res[k].end >= intervals[i].end else intervals[i].end)
            else:
                res.append(intervals[i])
                k += 1
            i += 1
        return res
