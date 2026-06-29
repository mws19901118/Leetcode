class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        return sum(int(x in word) for x in patterns)      #Check every string.
