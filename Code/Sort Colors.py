class Solution:
    # @param A a list of integers
    # @return nothing, sort in place
    def sortColors(self, A):
        i=0
        n=len(A)
        start=0
        end=n-1
        while i<n and i<=end:
            if A[i]==1:               #If current value is 1, simply increase i by 1.
                i+=1
            elif A[i]==0:             #If current value is 0, to move it to front, swap A[i] with A[start] and increase start by 1.
                A[i]=A[start]
                A[start]=0
                start+=1
                i+=1                  #We have to increase i by 1 here , because all the value in front of i is no greater than A[i], if we don't do this, it may result in incorrect growth of start and index out of bound.
            else:                     #If current value is 2, to move it to end, swap A[i] with A[end] and decrease end by 1.
                A[i]=A[end]
                A[end]=2
                end-=1
