from collections import defaultdict
class Solution:
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        wordsA = A.split(" ")                       #Split A by space.
        wordsB = B.split(" ")                       #Split B by space.
        dictA = defaultdict(int)
        dictB = defaultdict(int)
        for a in wordsA:                            #Count each word in A.
            dictA[a] += 1
        for b in wordsB:                            #Count each word in B.
            dictB[b] += 1
        result = []
        for a in dictA:
            if a not in dictB and dictA[a] == 1:    #If a word only appears only once in A and not in B, add to result. 
                result.append(a)
        for b in dictB:
            if b not in dictA and dictB[b] == 1:    #If a word only appears only once in B and not in A, add to result.
                result.append(b)
        return result
