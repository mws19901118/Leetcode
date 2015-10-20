class Solution:
    # @return a list of integers
    def grayCode(self, n):
        if n==0:                                              #If n equals 0, return [0].
            return [0]
        else:
            result=self.grayCode(n-1)                         #The first half of gray code sequence for n is the gray code sequence for n-1.
            length=2**(n-1)
            for i in range(length):
                result.append(length|result[length-1-i])      #The second half of gray code sequence for n is the reverse gray code sequence for n-1 bitwise ORed with 2^(n-1).
            return result
