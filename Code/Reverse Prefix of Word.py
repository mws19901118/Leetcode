class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        index = word.find(ch)                                  #Find the index of ch in word.
        return word[:index + 1][::-1] + word[index + 1:]       #Reverse the prefix ending at index and appending the rest then return.
