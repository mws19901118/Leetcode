class Solution:
    def isIdealPermutation(self, A: List[int]) -> bool:
        x = 0                                                               #To have equal global inversion and local inversion, All global inversion have to be local inversion so each inversion has to be the swap of 2 adjacent number.
        while x < len(A) - 1:                                               #Traverse A; since it's garunteed to be a permutation, we only need to valid the first N - 1 number.
            while x < len(A) - 1 and x == A[x]:                             #The sub array between each local inversion(including both ends) should be either empty or strictly in ascending order and the value equals its index.
                x += 1
            if x < len(A) - 1 and (A[x] != x + 1 or A[x + 1] != x):         #The inversion has to be the swap of 2 adjacent number; otherwise return false.
                return False
            x += 2                                                          #Move to next sub array.
        return True                                                         #Return true at the end.
