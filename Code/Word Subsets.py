class Solution:
    def isUniversal(self, w: str, counterUnion: Counter) -> bool:                                   #Determine if a is universal.
        counter = Counter(w)                                                                        #Get the counter of a.
        return all(counter[x] >= counterUnion[x] for x in counterUnion)                             #Return if all characters in counterBUnion has at least the same count in counterA as in counterB.
    
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        counterUnion = Counter()
        for w in words2:                                                                            #Union the character count of each word in words2.
            counter = Counter(w)
            for x in counter:
                counterUnion[x] = max(counterUnion[x], counter[x])
        return filter(lambda x: self.isUniversal(x, counterUnion), words1)                          #Return all the universal word in words1.
