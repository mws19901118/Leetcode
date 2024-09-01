class Trie:                                                        #Define trie node.
    def __init__(self, value):
        self.children = {}
        self.value = value

class FileSystem:

    def __init__(self):                                            #Initialize trie.
        self.trie = Trie(-1)

    def createPath(self, path: str, value: int) -> bool:
        chunks = path.split('/')[1:]                               #Split path.
        t = self.trie                                              #Get the root of trie.
        for i in range(len(chunks) - 1):                           #Traverse the parent paths.
            if chunks[i] in t.children:                            #If current parent path is in the children of t, move t to next level.
                t = t.children[chunks[i]]
            else:                                                  #Otherwise, return false.
                return False
        if chunks[-1] in t.children:                               #If the final path is already taken, return false.
            return False
        t.children[chunks[-1]] = Trie(value)                       #Create a new entry for the final path in the children of t.
        return True                                                #Return true.

    def get(self, path: str) -> int:
        chunks = path.split('/')[1:]                               #Split path.
        t = self.trie                                              #Get the root of trie.
        for i in range(len(chunks)):                               #Traverse the paths.
            if chunks[i] in t.children:                            #If current path is in the children of t, move t to next level.
                t = t.children[chunks[i]]
            else:                                                  #Otherwise, return -1.
                return -1
        return t.value                                             #Return the value found.


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)
