class Solution:
    def findSmallestRegion(self, regions: List[List[str]], region1: str, region2: str) -> str:
        parent = {}                                                                                        #Store the parent of each region.
        for r in regions:                                                                                  #Traverse each row in regions.
            for x in r[1:]:                                                                                #For every region in r[1:], its parent is r[0]
                parent[x] = r[0]
        
        def findPath(region: str) -> List[str]:                                                            #Find path from root to the region.
            curr = region                                                                                  #Initialize a pointer to region.
            path = [curr]                                                                                  #Initialize the path with region itself.
            while curr in parent:                                                                          #Iterate while curr in parent.
                path.append(parent[curr])                                                                  #Append parent[curr] to path.
                curr = parent[curr]                                                                        #Replace curr with parent[curr].
            path.reverse()                                                                                 #Reverse the path.
            return path

        region1Path, region2Path = findPath(region1), findPath(region2)                                    #Find the path for region1 and region2.
        i = 0
        while i < len(region1Path) and i < len(region2Path) and region1Path[i] == region2Path[i]:          #Find the first region that differs in 2 paths, could be none.
            i += 1
        return region1Path[i - 1]                                                                          #The the previous one is the smallest common region.
