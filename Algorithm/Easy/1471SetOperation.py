# Set就像是把Dict中的key抽出来了一样，类似于一个List，但是内容又不能重复 set集合是无序的
# 如果有需要求（集合，列表等）的并集和交集的时候，最好使用Set
class Solution:
    """
    @param A: The set A
    @param B: The set B
    @return: Return the size of three sets
    """
    def getAnswer(self, A, B):
        # Write your code here
        union=len(set(A).union(set(B)))
        intersection=len(set(A).intersection(set(B)))
        difference=len(set(A).difference(set(B)))
        return [union,intersection,difference]