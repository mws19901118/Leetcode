class Solution:
    # @param n, an integer
    # @return an integer
    def hammingWeight(self, n):
        b=bin(n)                      #Transform decimal number to binary number.
        count=0
        for i in range(len(b)):
            if b[i]=='1':             #Count the '1' bit.
                count+=1
        return count
