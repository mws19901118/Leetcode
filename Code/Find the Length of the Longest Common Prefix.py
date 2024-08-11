class Trie:                                                                         #Trie.
    def __init__(self):
        self.hasNode = False
        self.children = defaultdict(lambda: Trie())

    def insert(self, word) -> None:
        if not word:
            self.hasNode = True
            return
        self.children[word[0]].insert(word[1:])

class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        trie = Trie()
        for x in arr1:                                                              #Insert all numbers in arr1 to trie.
            trie.insert(str(x))
        result = 0
        for x in arr2:                                                              #Traverse arr2.
            node, index, s = trie, 0, str(x)                                        #Point node to trie root, convert s to string s and have a pointer to traverse s.
            while node and index < len(s) and s[index] in node.children:            #Iterate while node is not None and index does not reach the end of s and s[index] is in the children of node.
                node = node.children[s[index]]                                      #Move node to node.children[s[index]].
                index += 1                                                          #Increase index.
            result = max(result, index)                                             #Update result.
        return result
