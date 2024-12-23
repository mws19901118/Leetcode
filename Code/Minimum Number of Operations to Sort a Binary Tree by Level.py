# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        def minSwaps(numbers: List[Tuple]) -> int:                              #Given a list of index and value tuple, calculate the min swaps needed to sort the values.
            numbers.sort(key = lambda x: x[1])                                  #Sort by value in ascending order.
            visited = {i: False for i in range(len(numbers))}                   #Initially, mark all index unvisited.
            swaps = 0
            for i in range(len(numbers)):                                       #Traverse numbers.
                if visited[i] or numbers[i][0] == i:                            #If current index is visited or current index is same as the index in tuple, continue.
                    continue
                cycle_size = 0                                                  #Initialize the size of current cycle.
                j = i
                while not visited[j]:                                           #Iterate starting from i until reaching a visited index.
                    visited[j] = True                                           #Mark j as vistied.
                    j = numbers[j][0]                                           #Set j to index of tje tuple.
                    cycle_size += 1                                             #Increase cycle size.                                       
                swaps += cycle_size - 1                                         #Add cycle size minus 1 to swaps.
            return swaps                                                        #Return swaps.

        result = 0
        q = [root]
        while q:                                                                #BFS.
            result += minSwaps([(i, x.val) for i, x in enumerate(q)])           #Calculate the min swaps needed to sort current level and add to the result.
            newq = []
            for x in q:
                if x.left:
                    newq.append(x.left)
                if x.right:
                    newq.append(x.right)
            q = newq
        return result
