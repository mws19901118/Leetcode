class Solution:
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        increase, decrease = True, True   #Initialy, it's both monotone increasing and monotone decreasing.
        for i in range(1, len(A)):
            if A[i] > A[i - 1]:           #If current number is larger than the previous one, it's no longer monotone decreasing.
                decrease = False
            elif A[i] < A[i - 1]:         #If current number is smaller than the previous one, it's no longer monotone increasing.
                increase = False
        return increase or decrease
