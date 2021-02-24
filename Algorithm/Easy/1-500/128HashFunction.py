class Solution:
    """
    @param key: A string you should hash
    @param HASH_SIZE: An integer
    @return: An integer
    """

    def hashCode(self, key, HASH_SIZE):
        # write your code here
        # length = len(key)
        # sum = 0
        # for i in range(len(key)):
        #     sum += ord(key[i]) * pow(33,length-i-1)
        # print(sum)
        # return sum % HASH_SIZE
        value = 0
        for i in key:
            value = (ord(i) + value * 33) % HASH_SIZE
        return value
