class Solution:
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        result = [None] * len(A)    #Create a list with the same length of A.
        even, odd = 0, 1            #Even number starts with inde 0 while odd number starts with index 1.
        for a in A:
            if a % 2:               #For each number in A, if it's odd, put it in the current odd index of result and increase odd by 2.
                result[odd] = a
                odd += 2
            else:                   #For each number in A, if it's even, put it in the current even index of result and increase odd by 2.
                result[even] = a
                even += 2
        return result
