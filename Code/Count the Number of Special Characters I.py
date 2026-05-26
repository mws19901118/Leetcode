class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        s = set(word)                                                                                #Store unique characters in a set.
        return sum(chr(ord('a') + i) in s and chr(ord('A') + i) in s for i in range(26))             #Count the characters whose lower case and upper case are both in s.
