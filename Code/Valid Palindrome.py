class Solution:
    def isPalindrome(self, s: str) -> bool:
        characters = [c for c in s.lower() if c.isalnum()]                                                  #Convert to lower case and remove all non-alphanumeric characters.
        return all(characters[i] == characters[-(i + 1)] for i in range(len(characters) // 2))              #Check if it is palindrome.
