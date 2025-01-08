class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        return sum(int(len(x) <= len(y) and y[:len(x)] == y[-len(x):] == x) for i, x in enumerate(words) for _, y in enumerate(words[i + 1:]))    #Enumerate each pair, and return the count of pair x and y that x is both prefix and suffix of y.
