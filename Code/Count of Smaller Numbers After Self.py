class BST(object):                                              #Modify the basic BST node.
    def __init__(self, val, countself, countleft):
        self.val = val                                          #Store the value.
        self.countself = countself                              #Count the occurrence of value of current node.
        self.countleft = countleft                              #Count the occurrence of values in the left subtree of current node.
        self.left = None
        self.right = None

class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) == 0:
            return []
        root = BST(nums[-1], 1, 0)                              #Construct the root.
        result = [root.countleft]                               #Initialize the result list.
        for i in range(len(nums) - 2, -1, -1):                  #Traverse from right to left.
            temp = root
            sum = 0                                             #Record the sum of occurrences of numbers smaller than current number along the path.
            while temp != None:
                if temp.val > nums[i]:                          #If current number is smaller than the value of current node, we should go to the left child of current node.
                    temp.countleft += 1                         #Thus, there is a new occurrence in the left subtree of current node, we have to plus countleft by 1.
                    if temp.left is None:                       #If the left child is none, we construct the left child with current number.
                        temp.left = BST(nums[i], 0, 0)
                    temp = temp.left
                elif temp.val < nums[i]:                        #If current number is larger than the value of current node, we should go to the right child of current node.
                    sum += temp.countleft + temp.countself      #All the occurrences of value of current node and values in the left subtree of current node is smaller than current number, so we add countself and countleft to sum.
                    if temp.right is None:                      #If the left child is none, we construct the left child with current number.
                        temp.right = BST(nums[i], 0, 0)
                    temp = temp.right
                else:                                           #Otherwise, we found current number in BST.
                    sum += temp.countleft                       #All the values in the left subtree of current node is smaller than current number, so we add countleft to sum.
                    temp.countself += 1                         #Current number occur once more, increase countself by 1.
                    result.append(sum)                          #Append sum to result.
                    break                                       #Break.
        result.reverse()                                        #Reverse the result list.
        return result
