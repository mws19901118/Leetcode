class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)                 #Return if the word frequencies of s and t are equal.
