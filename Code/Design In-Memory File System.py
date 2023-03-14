class TreeNode:                                                                             #Tree node to store file or directory.
    def __init__(self, isFile: bool):
        self.content = "" if isFile else None                                               #Content is empty string initially if node is file; otherwise is none.
        self.children = None if isFile else {}                                              #Children is empty dictionary initially if not is directory; otherwise is none.

class FileSystem:

    def __init__(self):                                                                     #Initialize root for file system tree.
        self.root = TreeNode(False)

    def ls(self, path: str) -> List[str]:
        segments = self.parse(path)                                                         #Parse path.
        node = self.root
        for x in segments:                                                                  #Traverse file system tree to find the last node of path.
            node = node.children[x]
        return [segments[-1]] if node.content else sorted(node.children.keys())             #Return the file name as list if node is file; otherwise, return the sorted keys in children.

    def mkdir(self, path: str) -> None:
        segments = self.parse(path)                                                         #Parse path.
        node = self.root
        for x in segments:                                                                  #Traverse file system tree.
            if x not in node.children:                                                      #If current directory not exist, create it.
                node.children[x] = TreeNode(False)
            node = node.children[x]

    def addContentToFile(self, filePath: str, content: str) -> None:
        segments = self.parse(filePath)                                                     #Parse filePath.
        node = self.root
        for x in segments[:-1]:                                                             #Traverse file system tree to find the parent directory of file.
            node = node.children[x]
        if segments[-1] not in node.children:                                               #If file not exist, create a file node at the filePath.
            node.children[segments[-1]] = TreeNode(True)
        node.children[segments[-1]].content += content                                      #Append content to file.

    def readContentFromFile(self, filePath: str) -> str:
        segments = self.parse(filePath)                                                     #Parse filePath.
        node = self.root                                                                    #Traverse file system tree to find file.
        for x in segments:
            node = node.children[x]
        return node.content                                                                 #Return content.
        
    def parse(self, path: str) -> List[str]:                                                #Parse the path to segements.
        return [] if path == "/" else path.split('/')[1:]                                   #If path is root, return empty list; otherwise, return path.split('/')[1:].

# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)
