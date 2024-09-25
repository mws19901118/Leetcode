class Trie:                                                                                                      #Trie.
    def __init__(self):                    
        self.hasWord = False
        self.children = defaultdict(lambda: Trie())

    def insert(self, word) -> None:
        if not word:
            self.hasWord = True
            return
        self.children[word[0]].insert(word[1:])

class Solution:
    def longestWord(self, words: List[str]) -> str:
        trie = Trie()                                                                                           #Initialize root of trie.
        for s in words:                                                                                         #Insert all words that are shorted than the total number of words to trie; otherwise, the word  won't be a candidate.
            if len(s) <= len(words):
                trie.insert(s)
        result = ""                                                                                             #Initialize result to be empty string.
        for s in words:                                                                                         #Traverse words.
            node = trie                                                                                         #Point node to trie.
            index = 0                                                                                           #Traverse s.
            while node and index < len(s) and s[index] in node.children and (index == 0 or node.hasWord):       #Iterate while node is not none, index not reaching the end of s, s[index] is in node.children and either index is 0 or node has word. Then, the current prefix s[:index] is in trie.=.
                node = node.children[s[index]]                                                                  #Move node to ndoe.children[s[index]].
                index += 1                                                                                      #Increase index.
            if index == len(s):                                                                                 #If index reaches the end, s is a candidate.
                if len(s) > len(result) or (len(s) == len(result) and s < result):                              #If it is longer than current result or same length but is lexicographically smaller, replace result with s.
                    result = s
        return result
