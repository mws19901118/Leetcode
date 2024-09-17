class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        words1, words2 = Counter(s1.split(" ")), Counter(s2.split(" "))                                                                            #Count words in s1 and words in s2.
        return (set(x for x in words1 if words1[x] == 1) - words2.keys()) | (set(x for x in words2 if words2[x] == 1) - words1.keys())             #Find uncommon words.
