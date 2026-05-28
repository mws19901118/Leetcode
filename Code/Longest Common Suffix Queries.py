class Trie:                                                                                            #The Trie class.
    def __init__(self):
        self.children = defaultdict(lambda: Trie())
        self.index = None                                                                              #Store the smallest index of word with current prefix.
        self.length = 0                                                                                #Store the smallest word length of word with current prefix.

    def insert(self, s: str, index: int, length: int) -> None:
        if self.index is None or self.length > length:                                                 #If index is not set or the length in current node is greater then incoming word length, update index and length of current node.
            self.index = index
            self.length = length
        if not s:                                                                                      #If s is empty, return.
            return
        self.children[s[0]].insert(s[1:], index, length)                                               #Recursively insert s[1:] in self.children[s[0]].

    def find(self, s: str) -> int:
        return self.index if not s or s[0] not in self.children else self.children[s[0]].find(s[1:])   #Find the index of word with longest common suffix. If s in empty or s[0] is not in the childrens of current node, return index of current node; otherwise, recursively find s[1:] in self.children[s[0]].

class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        trie = Trie()                                                                                  #Initialize trie.
        for i, x in enumerate(wordsContainer):                                                         #Traverse wordsContainer.
            trie.insert(x[::-1], i, len(x))                                                            #Reverse x and insert it to the trie with i.
        return [trie.find(q[::-1]) for q in wordsQuery]                                                #For each query, reverse it and find index in trie. Then return the index list.
