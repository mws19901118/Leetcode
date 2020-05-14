class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict = {}
        self.hasWord = False

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        if len(word) == 0:
            self.hasWord = True                                                         #If the word ends, set the indicator to true.
            return
        if word[0] not in self.dict:                                                    #If current character is not in the dict, add it to the dict.
            self.dict[word[0]] = Trie()
        self.dict[word[0]].insert(word[1:])                                             #If the word doesn't end, insert its next character recursively.

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        if len(word) == 0:                                                              #If the word ends, return the indicator.
            return self.hasWord
        if word[0] not in self.dict:                                                    #If current character is not in the list, return false.
            return False
        return self.dict[word[0]].search(word[1:])                                      #If the word doesn't end, search its next character recursively.

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        if len(prefix) == 0:                                                            #If the prefix ends, return true.
            return True
        if prefix[0] not in self.dict:                                                  #If current character is not in the list, return false.
            return False
        return self.dict[prefix[0]].startsWith(prefix[1:])                              #Otherwise, search its next character recursively.


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
