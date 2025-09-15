class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        broken_set = set(brokenLetters)                                          #Store broken letters in a set.
        return sum(int(not set(w) & broken_set) for w in text.split(' '))        #Split text by space to get the word list and return the count of word which doesn't have broken letter in it.
