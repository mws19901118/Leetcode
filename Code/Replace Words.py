class Trie:                                                                                      #Trie node.
    def __init__(self):
        self.hasWord = False
        self.children = {}

    def insert(self, word: str) -> None:
        if not word:
            self.hasWord = True
            return
        if word[0] not in self.children:
            self.children[word[0]] = Trie()
        self.children[word[0]].insert(word[1:])
    
class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = Trie()                                                                            #Instantiate a trie.
        for word in dictionary:                                                                  #Insert all words in dictionary to trie.
            trie.insert(word)
        splited = sentence.split(' ')                                                            #Split sentence.
        result = []
        for word in splited:                                                                     #Traverse splited.
            node = trie                                                                          #Initialize a pointer to root of trie.
            index = 0                                                                            #Initialize a pointer at 0.
            while not node.hasWord and index < len(word) and word[index] in node.children:       #Iterate while node doesn't have word and index hasn't reach the end of word and word[index] is in the children of node.
                node = node.children[word[index]]                                                #Move node to node.children[word[index]].
                index += 1                                                                       #Also move forward index.
            result.append(word[:index] if node.hasWord else word)                                #If node has word, word[:index] is the shortest root of word, so add it to result; otherwise, add word to result.
        return " ".join(result)                                                                  #Join result with delimiter " " and return.
