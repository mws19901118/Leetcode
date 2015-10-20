class Solution:
    # @param grid, a list of list of characters
    # @return an integer
    def numIslands(self, grid):
        m=len(grid)
        if m==0:
            return 0
        n=len(grid[0])
        if n==0:
            return 0
        count=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]=='1':
                    queue=[(i,j)]                                                     #If current character is '1', append the coordinate to queue.
                    while queue!=[]:
                        c= queue.pop(0)                                               #Deque the first element, and set the corresponding character to '0', then do breadth-first search.
                        x=c[0]
                        y=c[1]
                        grid[x][y]='0'
                        if x-1>=0 and (x-1,y) not in queue and grid[x-1][y]=='1':
                            queue.append((x-1,y))
                        if x+1<m and (x+1,y) not in queue and grid[x+1][y]=='1':
                            queue.append((x+1,y))
                        if y-1>=0 and (x,y-1) not in queue and grid[x][y-1]=='1':
                            queue.append((x,y-1))
                        if y+1<n and (x,y+1) not in queue and grid[x][y+1]=='1':
                            queue.append((x,y+1))
                    count+=1                                                          #Count the number of islands.
        return count
