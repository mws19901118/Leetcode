class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        return sum(int(x.startswith(pref))for x in words)    #Count the word starting with prefix.
