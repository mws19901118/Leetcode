class Solution:
    def smallestRangeI(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        return max(max(A) - min(A) - 2 * K, 0)     #Calculate the the difference between max value of A and min value of A then minus twice of K.
                                                   #If the result is larger than 0, return result; else return 0.
