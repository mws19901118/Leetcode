class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        s = set(words)                                                        #Convert words to a set.
        return [x for x in words if any(x in y for y in (s - set([x])))]      #Find all words that are substrings of others.
