# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def nextLarger(self, root: Optional[TreeNode], stack: List[TreeNode]) -> TreeNode:              #Move to next larger node.
        curr = None
        if root.right:
            curr = root.right
            while curr.left:
                stack.append(curr)
                curr = curr.left
        else:
            curr = stack.pop()
        return curr
    
    def nextSmaller(self, root: Optional[TreeNode], stack: List[TreeNode]) -> TreeNode:             #Move to next smaller node.
        curr = None
        if root.left:
            curr = root.left
            while curr.right:
                stack.append(curr)
                curr = curr.right
        else:
            curr = stack.pop()
        return curr

    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        smallestStack, largestStack = [], []                                                        #Initialize stacks for smallest node and largest node.
        smallest, largest = root, root                                                              #Find the current smallest node and largest node.
        while smallest.left:
            smallestStack.append(smallest)
            smallest = smallest.left
        while largest.right:
            largestStack.append(largest)
            largest = largest.right

        while smallest.val < largest.val:                                                           #Traverse while smallest node is smaller than largest node.
            s = smallest.val + largest.val                                                          #Get the sum of smallest node and largest node.
            if s > k:                                                                               #If sum is larger than k, move largest node to its next smaller node.
                largest = self.nextSmaller(largest, largestStack)
            elif s < k:                                                                             #If sum is smaller than k, move smallest node to its next larger node.
                smallest = self.nextLarger(smallest, smallestStack)
            else:                                                                                   #If sum equals k, return true.
                return True
        return False                                                                                #Return false.
