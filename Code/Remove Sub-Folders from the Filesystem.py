class Trie:                                                            #Trie node.
    def __init__(self):
        self.hasFolder = False
        self.children = defaultdict(Trie)

    def insert(self, nodes: List[str]) -> None:
        if not nodes:
            self.hasFolder = True
            return
        self.children[nodes[0]].insert(nodes[1:])

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        trie = Trie()                                                  #Initialize the trie root.
        for i, x in enumerate(folder):                                 #Traverse folders.
            trie.insert(x.split("/")[1:])                              #Parse folder and insert path into trie with index.

        result, stack = [], [""]                                       #Initialize result; also initialize stack for DFS with an empty string representing the root node.
        def dfs(node: Trie) -> None:                                   #DFS.
            if not node:                                               #If node is none, return.
                return
            if node.hasFolder:                                         #If node has folder, join stack by "/" and append it to result; then return.
                result.append("/".join(stack))
                return
            for x in node.children:                                    #Traverse the children of node.
                stack.append(x)                                        #Append x to stack.
                dfs(node.children[x])                                  #Keep DFS in node.children[x].
                stack.pop()                                            #Pop stack.
        
        dfs(trie)                                                      #DFS from root.
        return result
