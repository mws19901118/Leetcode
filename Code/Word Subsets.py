class Solution:
    def isUniversal(self, a: str, counterBUnion: Counter) -> bool:                            #Determine if a is universal.
        counterA = Counter(a)                                                                 #Get the counter of a.
        return all(counterA[x] >= counterBUnion[x] for x in counterBUnion)                    #Return if all characters in counterBUnion has at least the same count in counterA as in counterBUnion.
    
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        counterBUnion = Counter()
        for w in B:                                                                           #Union the character count of each word in B.
            counterB = Counter(w)
            for x in counterB:
                counterBUnion[x] = max(counterBUnion[x], counterB[x])
        return [word for word in A if self.isUniversal(word, counterBUnion)]                  #Return all the universal word in A.
