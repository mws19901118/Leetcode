class Trie:                                                            #Trie node.
    def __init__(self):
        self.wordIndex = -1                                            #Link the trie node with the original index of folder.
        self.children = defaultdict(lambda: Trie())

    def insert(self, path: List[str], index: int) -> None:
        if not path:
            self.wordIndex = index
            return
        self.children[path[0]].insert(path[1:], index)

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        trie = Trie()                                                  #Initialize the trie root.
        for i, x in enumerate(folder):                                 #Traverse folders.
            trie.insert(x.split("/")[1:], i)                           #Parse folder and insert path into trie with index.

        result = []
        def dfs(stack: List['Trie']) -> None:                          #DFS.
            node = stack[-1]
            if node.wordIndex != -1:                                   #If current node is a complete folder, append the folder to result and return.
                result.append(folder[node.wordIndex])
                return
            for x in node.children.values():                           #Traverse the children of current node.
                stack.append(x)                                        #Append child to stack.
                dfs(stack)                                             #Keep DFS.
                stack.pop()                                            #Pop stack.

        dfs([trie])                                                    #Start DFS from trie root.
        return result
