class Solution:
    def minimumDeletions(self, s: str) -> int:
        countA, countB = sum(int(x == 'a') for x in s), 0          #Count 'a' after current index and 'b' on or before current index.
        result = countA                                            #Initially we can change all 'a' to 'b'.
        for x in s:                                                #Traverse s.
            countA -= int(x == 'a')                                #Update countA.
            countB += int(x == 'b')                                #Update countB.
            result = min(result, countA + countB)                  #We could change all A after current index to 'b' and all 'b' on or before current index to 'a'.
        return result
