class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxProduct(self, A):
        length=len(A)
        if length==0:
            return 0
        elif length==1:
            return A[0]
        ma=[0]*length                                     //ma[i] stores the max product end with A[i]
        mi=[0]*length                                     //mi[i] stores the min product end with A[i]
        ma[0]=A[0]
        mi[0]=A[0]
        maxP=A[0]
        for i in range(1,length):                         //DP in a loop
            ma[i]=max(A[i],ma[i-1]*A[i],mi[i-1]*A[i])     
            mi[i]=min(A[i],ma[i-1]*A[i],mi[i-1]*A[i])
            if ma[i]>maxP:
                maxP=ma[i]
        return maxP
