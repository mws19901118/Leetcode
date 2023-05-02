class Trie:                                                                                     #Trie.
    def __init__(self):
        self.hasWord = False
        self.children = defaultdict(list)

    def insert(self, word: str) -> None:                                                        #Insert word to trie.
        if not word:
            self.hasWord = True
            return
        if word[0] not in self.children:
            self.children[word[0]] = Trie()
        self.children[word[0]].insert(word[1:])

class Solution:
    def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:
        trie = Trie()                                                                           #Instentiate a trie.
        for x in words:                                                                         #Insert each word to trie.
            trie.insert(x)
        result = []                                                                             #Initialize result.
        for i in range(len(text)):                                                              #Traverse text.
            curr = trie                                                                         #Initialize a pointer to trie root.
            for j in range(i, len(text)):                                                       #Traverse each character in text[i:].
                if text[j] not in curr.children:                                                #If current character is not in curr.children, break.
                    break
                curr = curr.children[text[j]]                                                   #Move curr to next level.
                if curr.hasWord:                                                                #If curr has word, add [i, j] to result.
                    result.append([i, j])
        return result
