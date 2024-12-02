class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        for i, x in enumerate(sentence.split(' ')):    #Split sentence by space and traverse.
            if x.startswith(searchWord):               #If current word starts with searchWord, return i + 1.
                return i + 1
        return -1                                      #Return -1 if not found.
