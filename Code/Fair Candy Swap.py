class Solution:
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        sumA = sum(A)                               #Sum up the elements in A.
        sumB = sum(B)                               #Sum up the elements in B.
        diff = int(abs(sumA - sumB) / 2)            #Calculate the diff between the 2 elements should be swapped.
        setB = set(B)                               #Hash B in set.
        for a in A:
            if sumA < sumB and a + diff in setB:    #If sumA is smaller than sumB, find a + diff in B and return.
                return [a, a + diff]
            if sumA > sumB and a - diff in setB:    #If sumB is larger than sumB, find a - diff in B and return.
                return [a, a - diff]
        return []
