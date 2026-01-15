class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        segments = defaultdict(list)                               #Store horizontal segments by y coordinate.
        for x, y, l in squares:                                    #Traverse squares.
            segments[y].append((x, x + l, True))                   #Append the bottom edge segment of square to the list of y in segments; true means it's the start of a square.
            segments[y + l].append((x, x + l, False))              #Append the top edge segment of square to the list of y + l in segments; false means it's the end of a square.
        yScan = sorted(segments.keys())                            #Sort all y coordinates.
        segmentCount = {}                                          #Initialize segment count of current scan.
        areaPrefixSum, widths = [0.0], []                          #Initialize the area prefix sum at each scan, initially 0.0. Also initialize the segment widths at each scan; it is initialized as empty list because there is no segment at beginning.
        totalArea = 0.0                                            #Initialize total area.
        for i in range(len(yScan) - 1):                            #Traverse yScan.
            for left, right, flag in segments[yScan[i]]:           #Traverse segments in current scan.
                if flag:                                           #If it's start of sqaure, if not exist in segmentCount, initialize it; then, increse its count in segmentCount; 
                    if (left, right) not in segmentCount:
                        segmentCount[(left, right)] = 0
                    segmentCount[(left, right)] += 1
                else:                                              #Otherwise, it's end of sqaure, decrease it's count in segment; if count is 0, delete it from segmentCount.
                    segmentCount[(left, right)] -= 1
                    if segmentCount[(left, right)] == 0:
                        segmentCount.pop((left, right))
            existingSegments = sorted(segmentCount.keys())         #Sort existing segments in segmentCount.
            length, lastX = 0, -1                                  #Initialize total covered segment length and last x of current y scan.
            for left, right in existingSegments:                   #Traverse existingSegments.
                if right > lastX:                                  #If right > lastX, add right - max(lastX, left) to length and update lastX.
                    length += right - max(lastX, left)
                    lastX = right
            totalArea += length * (yScan[i + 1] - yScan[i])        #The area of total covered segment length from yScan[i] to yScan[i + 1] is covered by squares.
            areaPrefixSum.append(totalArea)                        #Append total area to areaPrefixSum.
            widths.append(length)                                  #Append length to widths.
        half = totalArea / 2                                       #Calculate half ot total area.     
        i = bisect.bisect_left(areaPrefixSum, ha;f) - 1            #Binary search half in areaPrefixSum to find the first index whose area is small than target.
        area = areaPrefixSum[i]                                    #Get the area.
        width = widths[i]                                          #Get the corresponding width.
        y = yScan[i]                                               #Get the corresponding y coordinate.
        return y + (half - area) / width                           #There might be remaning area need to be divided; so to split exactly, add (half - area) / width to y.
