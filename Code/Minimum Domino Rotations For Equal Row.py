class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        countAA, countAB, countBA, countBB = 0, 0, 0, 0                       #Only A[0] and B[0] are valid values. So, count the rotations of making A all equal to A[0], making A all equal to B[0], making B all eqaul to A[0], making B all eqaul to B[0] respectively.
        for a, b in zip(A, B):                                                #Traverse through A and B at the same time.
            if a != A[0] and b != A[0]:                                       #If neither of a and b is A[0], cannot make A all equal to A[0] or make B all equal to A[0].
                countAA = -1
                countBA = -1
            if a != B[0] and b != B[0]:                                       #If neither of a and b is B[0], cannot make A all equal to B[0] or make B all equal to B[0].
                countAB = -1
                countBB = -1
            countAA += a != A[0] and b == A[0] and countAA != -1              #While can make A all eqaul to A[0], we need to rotete if a is not A[0] and b is A[0].
            countAB += a != B[0] and b == B[0] and countAB != -1              #While can make A all eqaul to B[0], we need to rotete if a is not B[0] and b is B[0].
            countBA += b != A[0] and a == A[0] and countBA != -1              #While can make B all eqaul to A[0], we need to rotete if b is not A[0] and a is A[0].
            countBB += b != B[0] and a == B[0] and countBB != -1              #While can make A all eqaul to B[0], we need to rotete if b is not B[0] and a is B[0].
        result = 20000                                                        #Initialze result to be maximum value.
        for c in [countAA, countAB, countBA, countBB]:                        #Find the min value of rotations which are not -1.
            result = min(result, c if c > -1 else result)
        return -1 if result == 20000 else result                              #If all rotations are -1, return -1; otherwise return result.
