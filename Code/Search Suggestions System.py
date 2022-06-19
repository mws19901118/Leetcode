class Trie:
    def __init__(self):                                                                         #Initialize trie node.
        self.indexes = []                                                                       #Store indexes of words in current node.
        self.map = defaultdict(Trie)                                                            #Store trie nodes in next level.
    
    def insert(self, word: str, index: int) -> None:
        self.indexes.append(index)                                                              #Append word index to indexes list.
        if not word:                                                                            #If this is the end of word, return
            return
        self.map[word[0]].insert(word[1:], index)                                               #Add word to next level trie node.
        
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie = Trie()                                                                           #Initialize trie.
        products.sort()                                                                         #Sort products lexicographically.
        for i, p in enumerate(products):                                                        #Add each word and its index to trie.
            trie.insert(p, i)
        result = []                                                                             #Initialize result.
        for x in searchWord:                                                                    #Traverse searchWord.
            trie = trie.map[x]                                                                  #Go to next level trie node.
            result.append([products[i] for i in trie.indexes[:3]])                              #Append top 3 search results of current type to result.
        return result
