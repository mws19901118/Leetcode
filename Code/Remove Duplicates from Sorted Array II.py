class Solution:
    # @param A a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        n=len(A)
        if n==0:
            return 0
        dict={}                                   #Count the number of appearence.
        size=0
        for i in range(n):
            if not dict.has_key(A[i]):
                dict[A[i]]=1
                A[size]=A[i]                      #Let first 'size' items be items depulicated at most twice.
                size=size+1
            elif dict[A[i]]==1:
                dict[A[i]]=2
                A[size]=A[i]
                size=size+1
        return size
