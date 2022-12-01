class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])                                                #Store vowels.
        return sum(1 for x in s[:len(s) // 2] if x in vowels) == sum(1 for x in s[len(s) // 2:] if x in vowels)         #Return if first half and second half has same count of vowels.
