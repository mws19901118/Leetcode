class Solution(object):
    def maxTurbulenceSize(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        result = 1                                                      #Each single element is a turbulent subarray, so result is at least 1.
        i = 0
        while i < len(A) - 1:
            if A[i] == A[i + 1]:                                        #If A[i] == A[i + 1], A[i] cannot be the start of turbulent subarray longer than 1, so move to next element.
                i += 1
            else:
                sign = cmp(A[i + 1], A[i])                              #Get the sign of A[i + 1] - A[i]
                j = i
                while j < len(A) - 1 and A[j] * sign < A[j + 1] * sign: #Check it's in the same turbulent subarray until the subarray ends. To be in the same turbulent subarray, A[j] * sign < A[j + 1] * sign.
                    j += 1
                    sign = -sign                                        #Flip the sign.
                result = max(result, j - i + 1)                         #Update result.
                i = j                                                   #Move i to the end of current turbulent subarray to search for the next turbulent subarray.
        return result
