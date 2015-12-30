# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import heapq
class Solution(object):
    def traverse(self, root, row, column, height, listdict, heapdict):                  #Traverse through the tree recursively.
        if column not in listdict:                                                      #If current column hasn't occurred before, add a list of empty lists whose length is the height of the tree corresponding to the column in listdict.
            listdict[column] = [[] for i in range(height)]                              #Also add a empty heap to heapdict.
            heapdict[column] = []
        if listdict[column][row] == []:                                                 #If current row hasn't occurred in current column before, push the row into heaplist[column].
            heapq.heappush(heapdict[column], row)
        listdict[column][row].append(root.val)                                          #Append the value of current node to the row-th list of listdict[column].
        if root.left is not None:
            self.traverse(root.left, row + 1, column - 1, height, listdict, heapdict)   #Recursively traverse the left child of current node if it is not none. The row of left child is row + 1, column is column - 1.
        if root.right is not None:
            self.traverse(root.right, row + 1, column + 1, height, listdict, heapdict)  #Recursively traverse the right child of current node if it is not none. The row of right child is row + 1, column is column + 1.
            
    def height(self, root):                                                             #Calculate the height of the tree.
        if root is None:
            return 0
        return max(self.height(root.left), self.height(root.right)) + 1
        
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        listdict = {}                                                                   #Store the value correspoding to the column.
        heapdict = {}                                                                   #Store which rows in current column have value in ascending order.
        h = self.height(root)                                                           #Precompute the height of the tree.
        self.traverse(root, 0, 0, h, listdict, heapdict)                                #Traverse: root as column 0, row 0.
        result = []
        start = min(listdict.keys())                                                    #Get the min value of column.
        end = max(listdict.keys())                                                      #Get the max value of column.
        for i in range(start, end + 1):                                                 #Check every column from left to right.
            result.append([])
            while heapdict[i] != []:                                                    #Pop each row that containing values from heap until heap is empty.
                row = heapq.heappop(heapdict[i])
                result[i - start].extend(listdict[i][row])                              #Add the list of value of the certain column and row to result of current column.
        return result
