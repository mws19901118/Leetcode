class Trie:                                                             #Trie.
    def __init__(self):
        self.letters = {}
        self.hasWord = False
    
    def addWord(self, word: str) -> None:
        if not word:
            self.hasWord = True
            return
        if word[-1] not in self.letters:                                #Instead of ordering by prefix, ordering by suffix.
            self.letters[word[-1]] = Trie()
        self.letters[word[-1]].addWord(word[:-1])
        
class StreamChecker:

    def __init__(self, words: List[str]):
        self.history = []
        self.trie = Trie()                                              #Initialize trie.
        for w in words:                                                 #Add words to trie.
            self.trie.addWord(w)
        
    def query(self, letter: str) -> bool:
        t = self.trie                                                   #Get the root of trie.
        self.history.append(letter)                                     #Append current letter to history.
        for x in reversed(self.history):                                #Search for word.
            if t.hasWord:                                               #If current trie node has word, return true.
                return True
            elif x not in t.letters:                                    #If current character not in the dictionary of current trie node, return false.
                return False
            t = t.letters[x]                                            #Go to next level.
        return t.hasWord                                                #Return if final trie node has word.


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
