class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        lset, rset = set(leftChild), set(rightChild)                        #Convert leftChild and rightChild to set.
        q = [i for i in range(n) if i not in lset and i not in rset]        #Find the tree root which is neither in lset nor in rset.
        if len(q) > 1:                                                      #If there are more than 1 root, return false.
            return False
        visited = set(q)                                                    #Mark root as visited.
        while q:                                                            #BFS.
            newq = []
            for x in q:                                                     #Traverse current queue.
                left = leftChild[x]                                         #Find the left child of current node.
                if left != -1:                                              #Process if it is not -1.
                    if left in visited:                                     #If it is already visited, return False.
                        return False
                    newq.append(left)                                       #Append it to newq and mark it as visited.
                    visited.add(left)
                right = rightChild[x]                                       #Find the right child of current node.
                if right != -1:                                             #Process if it is not -1.
                    if right in visited:                                    #If it is already visited, return False.
                        return False
                    newq.append(right)                                      #Append it to newq and mark it as visited.
                    visited.add(right)
            q = newq                                                        #Replace q with newq.
        return len(visited) == n                                            #Return if all nodes are visited.
