class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        similarPairsSet = set([(x, y) for x, y in similarPairs] + [(y, x) for x, y in similarPairs])                                        #For each similar pair x and y, store (x, y) and (y, x) in a set.
        return len(sentence1) == len(sentence2) and all(x == y or (x, y) in similarPairsSet for x, y in zip(sentence1, sentence2))          #Return true if the lengths of sentence1 and sentence2 are same and all word pairs are in the set.
