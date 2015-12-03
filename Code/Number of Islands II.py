class Solution(object):
    class UnionFind(object):                                                                  #Union Find Data Strcture
        def __init__(self, x, y):
            self.x = x
            self.y = y
            self.parent = None
            
        def Find(self):                                                                       #Find the root of current node. 
            if self.parent != None:                                                           #If current node has parent, recursively find the root and then set parent as root.
                self.parent = self.parent.Find()
                return self.parent
            else:                                                                             #Otherwise, return current node itself.
                return self
        
        def Union(self, uf):                                                                  #Merge current node and another node.
            a = self.Find()                                                                   #Find the root of current node.
            b = uf.Find()                                                                     #Find the root of another node.
            if a is not b:                                                                    #If the 2 roots are not same, set the parent of root of another node as root of current node and return true.
                b.parent = a
                return True
            else:                                                                             #Otherwise, the 2 nodes have the same root, return false.
                return False
                
    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        dict = {}                                                                             #Use a dict to store UnionFind corresponding to coordinate.
        count = 0                                                                             #Count the number of islands.
        result = []                                                                           #Record the result after each operation.
        for coordinate in positions:                                                          #Get the coordinate of each operation.
            x = coordinate[0]
            y = coordinate[1]
            current = Solution.UnionFind(x, y)                                                #Create a new UnionFind.
            dict[(x, y)] = current                                                            #Store it in dictionary according to coordinate.
            count += 1                                                                        #Add 1 to the count of islands.
            for direction in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:                #Go through the 4 directions of current island.
                if direction in dict:                                                         #If it's island, find its root.
                    neighbor = dict[direction].Find()
                    if neighbor.Union(current):                                               #Merge current island and the neighbor, and if they don't have the same root, subtract count by 1.
                        count -= 1
            result.append(count)                                                              #Append count to result.
        return result
