class Trie:                                                                                    #Trie node class.
    def __init__(self):
        self.children = defaultdict(Trie)

    def insert(self, paths: List[str]) -> None:                                                #Insert to trie.
        if not paths:
            return
        self.children[paths[0]].insert(paths[1:])
    
    def serialize(self, count: Counter) -> str:                                                #Serialize the children of each node, not including itself; also count the serialization.
        self.serialization = ""                                                                #Initialize serialization to empty string.
        if not self.children:                                                                  #If no children, return current serialization.
            return self.serialization
        chunks = []                                                                            #Initialize chunks to store the serialization of each child.
        for x in self.children:                                                                #Traverse each child and recursively serialize each child, then wrap the serialization of each child with parenthese.
            chunks.append("(" + x + self.children[x].serialize(count) + ")")
        chunks.sort()                                                                          #Sort the chunks to rule out order problem.
        self.serialization = "".join(chunks)                                                   #Join chunks to get serialization for current node.
        count[self.serialization] += 1                                                         #Increase count of serialization.
        return self.serialization                                                              #Return current serialization.
    
    def dfs(self, count: Counter, result: List[str], stack: List[str]) -> None:                #DFS the trie to only return folders with no duplicates.
        if count[self.serialization] > 1:                                                      #If current serialization has appeared more than once, directly return to skip duplicate.
            return
        if stack:                                                                              #If stack is not empty(root), append the deepcopy of stack to result.
            result.append(deepcopy(stack))
        for x in self.children:                                                                #Traverse children.
            stack.append(x)                                                                    #Append current child to stack.
            self.children[x].dfs(count, result, stack)                                         #Keep DFS.
            stack.pop()                                                                        #Pop stack.

class Solution:
    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        trie = Trie()                                                                          #Initialize the root of trie.
        for p in paths:                                                                        #Traverse paths to insert each path to trie.
            trie.insert(p)
        count = Counter()
        trie.serialize(count)                                                                  #Serialize each node and count each serialization.
        result, stack = [], []
        trie.dfs(count, result, stack)                                                         #DFS to only return folders with no duplicates.
        return result
