class Solution:
    def removeVowels(self, s: str) -> str:
        return "".join([x for x in s if x not in "aeiou"])        #Remove 'a', 'e', 'i', 'o', 'u' from s.
