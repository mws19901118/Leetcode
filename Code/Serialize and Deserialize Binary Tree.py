# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:                                              #If root is none, return '#'.
            return "#"
        q = [root]                                                #Add root to queue.
        serial = [str(root.val)]                                  #Store the list of value.
        while q:                                                  #Serialize the tree level by level top down.
            newq = []                                             #Store the nodes in next level.
            for x in q:                                           #Check every nodes in current level.
                if not x.left:                                    #If its left child is none, append '#' to serial.
                    serial.append('#')
                else:                                             #Otherwise append the val of its left child to serial and add its left child to newq.
                    serial.append(str(x.left.val))
                    newq.append(x.left)
                if not x.right:                                   #If its right child is none, append '#' to serial.
                    serial.append('#')
                else:                                             #Otherwise append the val of its right child to serial and add its right child to newq.
                    serial.append(str(x.right.val))
                    newq.append(x.right)
            q = newq                                              #Replace q with newq.
        return ','.join(serial)                                   #Join the list by ',' and return it.

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == '#':                                           #If the first value is '#', return none.
            return None
        serial = data.split(',')                                  #Split the data by ',' and get the list of value.
        root = TreeNode(int(serial[0]))                           #Construct the root.
        q = [root]                                                #Store the nodes in current level.
        index = 1                                                 #Record current position in serial.
        while q and index < len(serial):                          #Construct the tree level by level top down.
            newq = []                                             #Store the nodes in next level.
            for x in q:                                           #Check every nodes in current level.
                if serial[index] != '#':                          #If its left child is not none, construct the left child according to correspoding value and append the left child to newq.
                    x.left = TreeNode(int(serial[index]))
                    newq.append(x.left)
                index += 1                                        #Go to the next value.
                if serial[index] != '#':                          #If its right child is not none, construct the right child according to correspoding value and append the right child to newq.
                    x.right = TreeNode(int(serial[index]))
                    newq.append(x.right)
                index += 1                                        #Go to the next value.
            q = newq                                              #Replace q with newq.
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
