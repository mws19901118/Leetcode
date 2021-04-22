class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        edges = defaultdict(int)                                      #Store count of edges by x coordinate, suppose left end of wall is 0. 
        for bricks in wall:                                           #Traverse each level.
            edge = 0                                                  #Initialize the right edge.
            for x in bricks[:-1]:                                     #Traverse current level until last element.
                edge += x                                             #Update right edge of current brick.
                edges[edge] += 1                                      #Add it to edges.
        return len(wall) - (max(edges.values()) if edges else 0)      #Return the height of wall minus max count in edges.
