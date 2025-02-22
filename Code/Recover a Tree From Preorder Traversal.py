# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        i = 0                                                            #Initialize index to traverse.
        while i < len(traversal) and traversal[i].isdigit():             #Find the root value.
            i += 1
        stack = [TreeNode(int(traversal[:i]))]                           #Create root and push it to an empty stack.
        while i < len(traversal):                                        #Traverse.
            j = i                                                        #Find the depth of next node.
            while j < len(traversal) and traversal[j] == '-':
                j += 1
            depth = j - i
            while stack and len(stack) > depth:                          #Pop stack until its length equals depth.
                stack.pop()
            i = j
            j = i                                                        #Find the value of next node.
            while j < len(traversal) and traversal[j].isdigit():
                j += 1
            node = TreeNode(int(traversal[i:j]))                         #Create a node with value.
            i = j
            if not stack[-1].left:                                       #If top of stack doesn't have left child, set its left child to node.
                stack[-1].left = node
            else:                                                        #Otherwise, set its right child to node.
                stack[-1].right = node
            stack.append(node)                                           #Append node to stack.
        return stack[0]                                                  #Return the first node in stack..
