class Solution:
    # @param A, a list of integers
    # @return a boolean
    def canJump(self, A):
        l=len(A)
        if l==1:                              #If A only contains 1 element, return true.
            return True
        end=0                                 #Use 'end' to indicate the max reachable index.
        for i in range(l-1):
            end=max(end,i+A[i])               #Traverse forward through each element and update 'end'.
            if end>=l-1:                      #If the last index is reachable, return true.
                return True
            if end==i:                        #If no further index is reachable at certain element, the jump game stucks, so return false.
                return False
