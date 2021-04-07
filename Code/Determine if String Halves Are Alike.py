class Solution:
    def countVowels(self, s: str) -> int:
        vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])                    #Store vowels.
        return sum(1 for i, x in enumerate(s) if x in vowels)                               #Count vowels in s.
        
    def halvesAreAlike(self, s: str) -> bool:
        return self.countVowels(s[:len(s) // 2]) == self.countVowels(s[len(s) // 2:])       #Return if first half and second half has same count of vowels.
