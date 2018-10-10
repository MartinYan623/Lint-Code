class Solution:
    """
    @param L: an integer
    @param R: an integer
    @return: the count of numbers in the range [L, R] having a prime number of set bits in their binary representation
    """
    def countPrimeSetBits(self, L, R):
        # Write your code here
        count=0
        for i in range(L,R+1):
            bits=0
            prime=True
            while i:
                if (i & 1)%2==1:
                    bits+=1
                i=i>>1
            if bits!=1:
                for j in range(2,bits):
                    if bits % j ==0:
                        prime=False
                        break
                if prime==True:
                    count+=1
        return count