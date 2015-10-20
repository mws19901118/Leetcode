class Solution:
    # @param A a list of integers
    # @param target an integer
    # @return a boolean
    def search(self, A, target):            #Though it's binary search, I don't think it's much faster than linear search.
        n=len(A)
        if n==0:
            return -1
        start=0
        end=n-1
        while start<=end:
            mid=(start+end)/2
            if A[mid]==target:
                return True
            elif A[mid]>target:             #Deal with the situation that A[mid]>target.
                if A[mid]<A[end]:           #If A[mid]<A[end], target is in the left side of mid.
                    end=mid-1
                elif A[mid]>A[end]:         #If A[mid]>A[end], the rotate pivot is in the right side of mid.
                    if A[start]>target:     #If A[start]>target, target is in the right side of mid; otherwise, target is in the left side of mid.
                        start=mid+1
                    else:
                        end=mid-1
                else:
                    if A[start]==A[end]:    #If A[start]=A[mid]=A[end], we can not determine which side target belongs to, so increase start by 1 and decrease end by 1.
                        start=start+1
                        end=end-1
                    else:                   #If A[mid]=A[end] but A[start]≠A[mid], target is in the left side of mid.
                        end=mid-1
            else:                           #The situation that A[mid]<target is just symmertric with the situation above.
                if A[mid]>A[start]:
                    start=mid+1
                elif A[mid]<A[start]:
                    if A[end]<target:
                        end=mid-1
                    else:
                        start=mid+1
                else:
                    if A[start]==A[end]:
                        start=start+1
                        end=end-1
                    else:
                        start=mid+1
        return False
