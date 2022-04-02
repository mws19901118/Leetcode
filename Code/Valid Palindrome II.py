class Solution:
    def validPalindrome(self, s: str) -> bool:
        start, end = 0, len(s) - 1                                                                             #2 pointers traverse from both ends to middle while characters on both pointer equal each other.
        while start < end and s[start] == s[end]:
            start += 1
            end -= 1
        return s[start + 1:end + 1] == s[start + 1:end + 1][::-1] or s[start:end] == s[start:end][::-1]       #If s[start + 1:end + 1] or s[start:end] is palindrome, s is a palindrome after deleting at most one character.
