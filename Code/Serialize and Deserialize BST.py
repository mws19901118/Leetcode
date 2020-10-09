# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        if root is None:                                                                #If root is none, return empty string.
            return ""
        left = self.serialize(root.left)                                                #Serialize left subtree.
        right = self.serialize(root.right)                                              #Serialize right subtree.
        return str(root.val) + "-" + str(len(left)) + "#" + left + "#" + right          #Serialize root with root value and length of left subtree serialization delimited by "-". Then delimit root and left subtree and right subtree with "#".

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        if data == "":                                                                  #If data is empty string, return none.
            return None
        index = data.find("#")                                                          #Find the first index of delimiter "#".
        node = data[:index].split("-")                                                  #From beginning to first delimiter "#", it's root. Then split root by delimiter "-".
        root = TreeNode(int(node[0]))                                                   #Create root node with root value(int before "-").
        length = int(node[1])                                                           #Get the length of left subtree serialization(int after "-")
        root.left = self.deserialize(data[index + 1:index + 1 + length])                #Deserialize left subtree, the substring after first delimiter "#" with above length.
        root.right = self.deserialize(data[index + 2 + length:])                        #Deserialize right subtree, the remaining subtree.
        return root                                                                     #Return root.
        

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans
