class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        s = set(x for x in allowed)                                  #Store characters in allowed in a set.
        return sum(int(all(x in s for x in w)) for w in words)       #Count word in words that all characters are in allowed.
