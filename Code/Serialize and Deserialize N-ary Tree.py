"""
# Definition for a Node.
class Node(object):
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        if children is None:
            children = []
        self.val = val
        self.children = children
"""

class Codec:
    def serialize(self, root: 'Node') -> str:
        """Encodes a tree to a single string.
        
        :type root: Node
        :rtype: str
        """
        if not root:                                                                  #If root is none, return empty string.
            return ""
        result = []                                                                   #Initialize result.
        q = [root]                                                                    #Traverse tree using BFS.
        while q:
            newq, level = []. []                                                      #Initialize newq and serialized nodes list for each level.
            for x in q:                                                               #Traverse q.
                level.append(str(x.val) + "_" + str(len(x.children)))                 #Serialize current node; basically use '_' to delimit node value and children count.
                newq.extend(x.children)
            result.append("#".join(level))                                            #Use '#' to delimit each node and append current level to result.
            q = newq
        return "/".join(result)                                                       #Use '/' to delimit each level.
	
    def deserialize(self, data: str) -> 'Node':
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: Node
        """
        if not data:                                                                  #If data is empty string, return none.
            return None
        levels = data.split('/')                                                      #Split by '/' to get each level.
        root, count = self.parse(levels[0])                                           #Parse the first level to get root and children count of root.
        q = [(root, count)]                                                           #Put them in a queue.
        for level in levels[1:]:                                                      #Traverse the rest of levels.
            nodes = level.split('#')                                                  #Split by '#' to get nodes in current level.
            newq, index = [], 0                                                       #Initialize new queue and index to traverse nodes.
            for parent, parentChildrenCount in q:                                     #Traverse queue to process each parent.
                for _ in range(parentChildrenCount):                                  #Process the next parentChildrenCount nodes in current level.
                    node, count = self.parse(nodes[index])                            #Parse current node.
                    newq.append((node, count))                                        #Append it to newq.
                    parent.children.append(node)                                      #Append node to the children of parent node.
                    index += 1
            q = newq                                                                  #Replace q with newq.
        return root                                                                   #Return root.
    
    def parse(self, nodeData: str) -> ('Node', count):                                #Parse each node.
        node = Node()                                                                 #Initialize node.
        index = nodeData.find('_')                                                    #Find the index of delimiter.
        node.val, count = int(nodeData[:index]), int(nodeData[index + 1:])            #Update node value and children count.
        return (node, count)                                                          #Return node and children count.

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
