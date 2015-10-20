class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        n=len(A)
        if n==0:
            return 0
        size=0                            #Record the length of array without duplicates.(Begin counting at 0, so plus 1 in the end.)
        for i in range(n):
            if A[size]!=A[i]:             #Do not remove items actually, just let the first 'size' items be distinct.
                size+=1                   #If encounter a new item, increase size by 1 and let A[size] be the new distinct item.
                A[size]=A[i]
        return size+1
