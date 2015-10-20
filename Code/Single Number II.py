class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        dict={}
        for i in xrange(0,len(A)):
            if dict.has_key(A[i]):
                dict[A[i]]+=1
            else:
                dict[A[i]]=1
        for num,count in dict.items():
            if count!=3:
                return num
