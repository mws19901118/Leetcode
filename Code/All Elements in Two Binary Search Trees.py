# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        stack1, stack2, output = [], [], []                                         #Initialize stack1 for traversing root1 and stack2 for traversing root2; also initialize output list.
        while root1 or root2 or stack1 or stack2:                                   #Traverse root1 and root2 simultaneously until finishing traversing in both trees.
            while root1:                                                            #Go to the left most node in root1 and append all nodes on the path to stack1.
                stack1.append(root1)
                root1 = root1.left
            while root2:                                                            #Go to the left most node in root2 and append all nodes on the path to stack2.
                stack2.append(root2)
                root2 = root2.left
                
            if not stack2 or stack1 and stack1[-1].val <= stack2[-1].val:           #If finished traversing root2 or the current value in root1 is smaller than current value in root2, append current value in root1 to output then pop stack1 and go to its right child.
                output.append(stack1[-1].val)
                root1 = stack1.pop().right
            else:                                                                   #Otherwise, append current value in root2 to output then pop stack2 and go to its right child.
                output.append(stack2[-1].val)
                root2 = stack2.pop().right

        return output
