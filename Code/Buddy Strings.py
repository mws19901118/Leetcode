class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) != len(B):                                                                    #The length of A and B must be equal.
            return False
        d = []
        for i in range(len(A)):                                                                 #Find all the different characters paires of A and B in same index.
            if A[i] != B[i]:
                d.append((A[i], B[i]))
        if len(d) == 0:                                                                         #If A and B are same, both strings must contain a character which appears more than once.
            countA, countB = Counter(A), Counter(B)
            return any(x in countB and countA[x] >= 2 and countB[x] >= 2 for x in countA)
        return len(d) == 2 and (d[0][0] == d[1][1] and d[0][1] == d[1][0])                      #If A and B are not same, there must be exactly 2 different characters paires. And they are able to swap.
