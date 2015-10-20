class Solution:
    # @param A  a list of integers
    # @param m  an integer, length of A
    # @param B  a list of integers
    # @param n  an integer, length of B
    # @return nothing
    def merge(self, A, m, B, n):
        i=0
        j=0
        while i<len(A) and j<n:                 #Ensure no index out of bound.
            if A[i]>=B[j]:
                A.insert(i,B[j])                #Insert B[j] at proper position.
                j+=1
            i+=1
        while j<n:
            A.insert(m+j,B[j])                  #Insert the rest of B.
            j+=1
