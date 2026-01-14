class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        segments = defaultdict(list)                                              #Store vertical segments by x coordinate.
        for left, bottom, right, top in rectangles:                               #Traverse rectangels.
            segments[left].append((bottom, top, True))                            #Append the left edge segment of rectangle to the list of left in segments; true means it's the start of rectangle.
            segments[right].append((bottom, top, False))                          #Append the right edge segment of rectangle to the list of right in segments; false means it's the end of rectangle.
        xScan = sorted(segments.keys())                                           #Sort all x coordinates.
        segmentCount = {}                                                         #Initialize segment count of current scan.
        area, division  = 0, 10 ** 9 + 7                                          #Initialize area and division.
        for i in range(len(xScan) - 1):                                           #Scan by x coordinates from left to right.
            for bottom, top, flag in segments[xScan[i]]:                          #Traverse segments in current scan.
                if flag:                                                          #If it's start of rectangle, if not exist in segmentCount, initialize it; then, increse its count in segmentCount; 
                    if (bottom, top) not in segmentCount:
                        segmentCount[(bottom, top)] = 0
                    segmentCount[(bottom, top)] += 1
                else:                                                             #Otherwise, it's end of rectangle, decrease it's count in segment; if count is 0, delete it from segmentCount.
                    segmentCount[(bottom, top)] -= 1
                    if segmentCount[(bottom, top)] == 0:
                        currentSegment.pop((bottom, top))
            existingSegments = sorted(segmentCount.keys())                        #Sort existing segments in segmentCount.
            length, maxY = 0, -1                                                  #Initialize total covered segment length and max y of current x scan.
            for bottom, top in existingSegments:                                  #Traverse existingSegments.
                if top > maxY:                                                    #If top > maxY, add top - max(maxY, bottom) to length and update maxY.
                    length += top - max(maxY, bottom)
                    maxY = top
            area = (area + length * (xScan[i + 1] - xScan[i])) % division         #The area of total covered segment length from xScan[i] to xScan[i + 1] is covered by rectangles. So increase area and calculate the modolo to 10 ** 9 + 7 to update area. 
        return area                                                               #Return area.
