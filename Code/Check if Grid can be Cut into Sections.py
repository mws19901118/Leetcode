class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        horizontal, vertical = [], []                          #Initialize list for horizontal points and vertical points.
        for start_x, start_y, end_x, end_y in rectangles:      #Traverse rectangles.
            horizontal.append((end_x, -1))                     #Append end_x to horizontal with tag -1.
            horizontal.append((start_x, 1))                    #Append start_x to horizontal with tag 1.
            vertical.append((end_y, -1))                       #Append end_y to vertical with tag -1.
            vertical.append((start_y, 1))                      #Append start_y to vertical with tag 1.
        
        def canCut(points: List[int]) -> bool:                 #Determine if a list of points can be cut into 3 sections.
            points.sort()                                      #Sort points.
            count, section = 0, 0                              #Intialize count of current rectangles and section.
            for x, t in points:                                #Traverse points.
                count += t                                     #Add tag to count.
                section += (not count)                         #If count is 0 then current coordinate does not cross any section; thus it is an end of a section.
            return section >= 3                                #Return if there are at least 3 sections.

        return canCut(horizontal) or canCut(vertical)          #Return true if it the rectangles can be cut horizontally or vertically.
