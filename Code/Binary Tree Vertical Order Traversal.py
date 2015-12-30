class Solution(object):
    def traverse(self, root, row, column, dict):                    #Traverse through the tree recursively.
        if root is None:
            return
        if column not in dict:                                      #If current column hasn't occurred before, add a new dict corresponding to current column.
            dict[column] = {}
        if row not in dict[column]:                                 #If current row hasn't occurred in current column, add a new list corresponding to current column and current row.
            dict[column][row] = []
        dict[column][row].append(root.val)                          #Append the value of root according to column and row.
        self.traverse(root.left, row + 1, column - 1, dict)         #Recursively traverse the left child of current node; its row is row + 1; its column is column - 1.
        self.traverse(root.right, row + 1, column + 1, dict)        #Recursively traverse the right child of current node; its row is row + 1; its column is column + 1.
        
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        dict = {}                                                   #Store value according to column and row.
        self.traverse(root, 0, 0, dict)                             #Traverse starting from root as column 0, row 0.
        result = []
        startc = min(dict.keys())                                   #Get the min value of column
        endc = max(dict.keys())                                     #Get the max value of column
        for i in range(startc, endc + 1):                           #Check every column.
            result.append([])
            startr = min(dict[i].keys())                            #Get the min value of row in current column.
            endr = max(dict[i].keys())                              #Get the max value of row in current column.
            for j in range(startr, endr + 1):
                if j in dict[i]:
                    result[i - startc].extend(dict[i][j])           #Add the list of value of the certain column and row to the end of result of current column.
        return result
