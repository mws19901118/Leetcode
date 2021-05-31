class Trie:
    def __init__(self):                                                                       #Initialize trie node.
        self.words = []                                                                       #Store words in current node.
        self.map = defaultdict(Trie)                                                          #Store trie nodes in next level.
    
    def addWord(self, index: int, word: str) -> None:
        self.words.append(word)                                                               #Append word to words list of current node.
        if index == len(word):                                                                #If reaches the end of word, return.
            return
        self.map[word[index]].addWord(index + 1, word)                                        #Add word to next level trie node.
        
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie = Trie()                                                                         #Initialize trie.
        products.sort()                                                                       #Sort products lexicographically.
        for p in products:                                                                    #Add each word to trie.
            trie.addWord(0, p)
        result = []                                                                           #Initialize result.
        for x in searchWord:
            result.append(trie.map[x].words[:3])                                              #Append top 3 search results of current type to result.
            trie = trie.map[x]                                                                #Go to next level trie node.
        return result
