class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        r=0
        for i in xrange(0,len(A)):
            r=r^A[i]                                    #bitwise operation
        return r
