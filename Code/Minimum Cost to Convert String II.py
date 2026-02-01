class Trie:                                                                                                                    #Trie class.
    def __init__(self):
        self.children = defaultdict(lambda: Trie())
        self.hasWord = False
    
    def insert(self, word: str) -> None:
        if not word:
            self.hasWord = True
            return
        self.children[word[0]].insert(word[1:])

class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        keys = list(set(original + changed))                                                                                   #Store all strings in original and changed in a list after de-duping.
        index = {x:i for i, x in enumerate(keys)}                                                                              #Build a map from key to its index.
        n = len(keys)
        matrix = [[inf] * n for _ in range(n)]                                                                                 #Initialize the distance matrix.
        for i in range(n):
            matrix[i][i] = 0
        for x, y, c in zip(original, changed, cost):                                                                           #Populate the distance matrix.
            matrix[index[x]][index[y]] = min(matrix[index[x]][index[y]], c)
        
        for k in range(n):                                                                                                     #Update the distance matrix with  Floyd-Warshall algorithm.
            for i in range(n):
                if matrix[i][k] < inf:
                    for j in range(n):
                        if matrix[k][j] < inf:
                            matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])

        sourceTrie, targetTrie = Trie(), Trie()                                                                                #Build source trie and target trie.
        for x, y in zip(original, changed):
            sourceTrie.insert(x)
            targetTrie.insert(y)
        
        @cache                                                                                                                 #Cache dp result.
        def dp(i: int) -> int:                                                                                                 #DP to calculate the min cost of converting source[i:] and target[i:].
            if i == len(source):
                return 0
            result = dp(i + 1) if source[i] == target[i] else inf                                                              #Initialize result to be dp(i + 1) if source[i] == target[i]; otherwise inf.
            st, tt = sourceTrie, targetTrie                                                                                    #Get references to the source trie and the target trie.
            j = i
            while len(st.children) > 0 and len(tt.children) > 0 and j < len(source):                                           #Traverse while j hasn't reached the end and both source trie and target trie has children.
                if st.children[source[j]].hasWord and tt.children[target[j]].hasWord:                                          #If the source trie has word at source[j] and target trie has word at target[j], we can convert source[i:j + 1] to target[i:j + 1].
                    result = min(result, matrix[index[source[i:j + 1]]][index[target[i:j + 1]]] + dp(j + 1))                   #Update result if the conversion cost plus dp(j + 1) is smaller.
                st, tt = st.children[source[j]], tt.children[target[j]]                                                        #Go to the next node in the source trie and the target trie.
                j += 1
            return result
        result = dp(0)                                                                                                         #Get the result of dp(0).
        return result if result < inf else -1                                                                                  #Return result if it is not inf; otherwise, return -1.
