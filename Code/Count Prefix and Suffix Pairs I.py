class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        return sum(int(y.startswith(x) and y.endswith(x)) for i, x in enumerate(words) for _, y in enumerate(words[i + 1:]))    #Enumerate each pair, and return the count of pair x and y that x is both prefix and suffix of y.
