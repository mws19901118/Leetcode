class Trie:                                                              #Trie class.
    def __init__(self):
        self.words = {}
        self.hasWord = False

    def insert(self, word: str) -> None:
        if not word:
            self.hasWord = True
            return
        if word[0] not in self.words:
            self.words[word[0]] = Trie()
        self.words[word[0]].insert(word[1:])

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        trie = Trie()                                                    #Instentiate a trie.
        for x in dictionary:                                             #Insert all words in dictinary to trie.
            trie.insert(x)
        
        @cache                                                           #Cache result.
        def dp(index: int) -> int:                                       #DP to find the min extra characters in dp[index:].
            if index == len(s):                                          #If index reaches the end of s, return 0.
                return 0
            extra = 1 + dp(index + 1)                                    #Initialize extra characters to be the result of use current character as extra character.
            t = trie                                                     #Pointer to current trie node.
            i = index                                                    #Point i to index.
            while i < len(s):                                            #Traverse from index to the end of s.
                if s[i] not in t.words:                                  #If s[i] is not in current trie node, break because we cannot find any i that s[index:i] is in dictionary.
                    break
                t = t.words[s[i]]                                        #Move trie node to next level.
                i += 1                                                   #Move forward i.
                if t.hasWord:                                            #If current trie node has word, s[index:i] is a word in dictionary, so update extra if dp(i) is smaller.
                    extra = min(extra, dp(i))
            return extra                                                 #Return extra.
        return dp(0)                                                     #Return dp(0).
