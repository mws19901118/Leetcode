class Solution:
    def dfs(self, index: int, edges: defaultdict(list), length: List[int]) -> int:
        if length[index]:                                                               #If current index is visited, directly return its longest string chain length.
            return length[index]
        length[index] = 1                                                               #Set length[index] to 1 as if the string chain only has itself.
        for x in edges[index]:                                                          #Traverse all adjacent indexes, and keep updating length[index]
            length[index] = max(length[index], self.dfs(x, edges, length) + 1)
        return length[index]                                                            #Return length[index]/
    
    def longestStrChain(self, words: List[str]) -> int:
        indexes = {w: i for i, w in enumerate(words)}                                   #Create a index by word map.
        edges = defaultdict(list)                                                       #Initialize edges adjacent list.
        for i, w in enumerate(words):                                                   #Traverse words.
            for j in range(len(w)):                                                     #Try remove each character in w.
                x = w[:j] + w[j + 1:]                                                   #Construct the new word after removing character.
                if x in indexes:                                                        #If the new word is in indexes, there is an edge from indexes[x] to i.
                    edges[indexes[x]].append(i)
        length = [0] * len(words)                                                       #Initialize the longest string chain length starting at each index.
        result = 0
        for i in range(len(words)):                                                     #DFS at each index and keep updating max length.
            result = max(result, self.dfs(i, edges, length))
        return result
