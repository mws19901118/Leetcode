class Trie:                                                                                                                                                     #Use trie to store max index for the pairs of (prefix, suffix) letter at same distance from end.
    def __init__(self):
        self.map = {}
        self.letters = 'abcdefghijklmnopqrstuvwxyz'                                                                                                             #Store letters.
    
    def insert(self, pairs: List[tuple], index: int) -> None:                                                                                                   #Insert pairs into trie.
        if not pairs:                                                                                                                                           #If pairs is empty, return.
            return
        if pairs[0] not in self.map:                                                                                                                            #If the first pair not in map, insteniate the max index and node to next level pair.  
            self.map[pairs[0]] = [-1, Trie()]
        self.map[pairs[0]][0] = index                                                                                                                           #Since we always insert pairs of word from small index to large index, keep update index to the latest.
        self.map[pairs[0]][1].insert(pairs[1:], index)                                                                                                          #Insert remaining pairs.
    
    def find(self, pairs: str) -> int:
        if not pairs:                                                                                                                                           #If no more pairs, return -1.
            return -1
        expandedPairs = [pairs[0]]                                                                                                                              #Expand pairs[0] in case prefix or suffix in pair is none; otherwise it only has pairs[0].
        if not pairs[0][0]:                                                                                                                                     #If prefix is none, match any pair in current node with this suffix.
            expandedPairs = [(x, pairs[0][1]) for x in self.letters]
        elif not pairs[0][1]:                                                                                                                                   #If suffix is none, match any pair in current node with this prefix.
            expandedPairs = [(pairs[0][0], x) for x in self.letters]

        result = -1                                                                                                                                             #Initialize result.
        for p in expandedPairs:                                                                                                                                 #Traverse expandedPairs.
            if p in self.map:                                                                                                                                   #If p is in self.map, there are words with given prefix and suffix so far.
                result = max(result, self.map[p][0] if len(pairs) == 1 else self.map[p][1].find(pairs[1:]))                                                     #If pairs has only pair, result is the index in map; otherwise, keep finding pairs[1:] recursively.
        return result                                                                                                                                           #Return the max result from traverse.

class WordFilter:

    def __init__(self, words: List[str]):
        self.trie = Trie()                                                                                                                                      #Instantiate trie. 
        for i, w in enumerate(words):                                                                                                                           #Traverse words.
            pairs = [(w[j], w[-(j + 1)]) for j in range(len(w))]                                                                                                #For each word, generate paris of (prefix, suffix) letter at same distance from end.
            self.trie.insert(pairs, i)                                                                                                                          #Insert pairs.

    def f(self, prefix: str, suffix: str) -> int:
        pairs = [(prefix[i] if i < len(prefix) else None, suffix[-(i + 1)] if i < len(suffix) else None) for i in range(max(len(prefix), len(suffix)))]         #Generate paris of (prefix, suffix) letter at same distance from end; if any prefix letter has no corrsponding suffix letter or vice versa, pad the pair with none.
        return self.trie.find(pairs)                                                                                                                            #Return the result of find pairs from trie.

# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)
