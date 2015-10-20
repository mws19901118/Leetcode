class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return an integer
    def search(self, A, target):
        n=len(A)
        if n==0:
            return -1
        start=0
        end=n-1
        while start<=end:
            mid=(start+end)/2
            if A[mid]==target:
                return mid
            else:
                if A[mid]>=A[start] and A[mid]<=A[end]:           #If A[start]<=A[mid]<=A[end], it's a normal binary search.
                    if A[mid]>target:
                        end=mid-1
                    else:
                        start=mid+1
                elif A[mid]>=A[start] and A[mid]>A[end]:          #If A[mid]>=A[start] and A[mid]>A[end], the rotate pivot is the right side of mid.
                    if target>=A[start] and target<A[mid]:        #If A[start]<=target<A[mid], target is in the left side of mid; otherwise, target is in the right side of mid.
                        end=mid-1
                    else:
                        start=mid+1
                elif A[mid]<A[start] and A[mid]<=A[end]:          #If A[mid]<A[start] and A[mid]<=A[end], the rotate pivot is the left side of mid.
                    if target<=A[end] and target>A[mid]:          #If A[mid]<target<=A[end], target is in the right side of mid; otherwise, target is in the left side of mid.
                        start=mid+1
                    else:
                        end=mid-1
        return -1                                                 #If can not find target, return -1.
