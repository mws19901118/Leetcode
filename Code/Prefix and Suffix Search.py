class Trie:                                                                                                     #Use trie to store the indexes of words which has certain prefix.
    def __init__(self):
        self.map = {}                                                                                           #Initialize map for current node.
    
    def insert(self, word: str, index: int) -> None:                                                            #Insert word into trie.
        if not word:                                                                                            #If word is empty, return.
            return
        if word[0] not in self.map:                                                                             #If the first letter not in map, create an entry(a list for indexes and a Trie for next node) in map for it.
            self.map[word[0]] = ([], Trie())
        self.map[word[0]][0].append(index)                                                                      #Append index to the list.
        self.map[word[0]][1].insert(word[1:], index)                                                            #Insert word[1:] in next node recursively.
    
    def find(self, prefix: str) -> List[int]:                                                                   #Find the list of indexes for given prefix.
        if not prefix or prefix[0] not in self.map:                                                             #If prefix is empty or the first letter not in map, return empty list.
            return []
        return self.map[prefix[0]][0] if len(prefix) == 1 else self.map[prefix[0]][1].find(prefix[1:])          #If prefix has only one letter, return the list in map; otherwise, return the result of prefix[1:] recursively.
    
class WordFilter:

    def __init__(self, words: List[str]):
        self.prefixTree = Trie()                                                                                #Initalize trie for prefix.
        self.suffixTree = Trie()                                                                                #Initalize trie for suffix.
        for i, w in enumerate(words):                                                                           #Traverse words.
            self.prefixTree.insert(w, i)                                                                        #Insert word to prefix tree.
            self.suffixTree.insert(w[::-1], i)                                                                  #Insert the reverse of word to suffix tree.

    def f(self, prefix: str, suffix: str) -> int:
        prefixIndexes = self.prefixTree.find(prefix)                                                            #Find the indexes from prefix tree.
        suffixIndexes = self.suffixTree.find(suffix[::-1])                                                      #Find the indexes from suffix tree.
        i, j = len(prefixIndexes) - 1, len(suffixIndexes) - 1
        while i >= 0 and j >= 0:                                                                                #Traverse 2 lists to find the largest common index and return.
            if prefixIndexes[i] > suffixIndexes[j]:
                i -= 1
            elif prefixIndexes[i] < suffixIndexes[j]:
                j -= 1
            else:
                return prefixIndexes[i]
        return -1                                                                                               #If not found, return -1.

# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)
