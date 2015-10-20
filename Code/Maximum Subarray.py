class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxSubArray(self, A):
        if len(A)==0:
            return 0
        if len(A)==1:
            return A[0]
        csum=A[0]                           #Record the max sum of subarray ending at each element. 
        maxsum=A[0]
        for i in range(1,len(A)):
            csum=max(csum+A[i],A[i])        #The max sum of subarray ending at current element equals the greater value of A[i] and the max sum of subarray ending at previous element plus A[i].
            if csum>maxsum:                 #If max sum of subarray ending at current element is greater than maxsum, update maxsum.
                maxsum=csum
        return maxsum
