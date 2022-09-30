#Divide and conquer solution:
class Solution:
    def appendToResult(self, result: List[List[int]], current: List[int]) -> None:
        if not result or result[-1][1] != current[1]:                                       #Current height cannot be same as previous height in result, if result is not empty.
            result.append(current)

    def merge(self, left: List[List[int]], right: List[List[int]]) -> List[List[int]]:
        i, j, h1, h2 = 0, 0, 0, 0                                                           #h1 represents the current height from the left skyline; h2 represent the current height from the right skyline.
        result = []
        while i < len(left) and j < len(right):                                             #Compare points of left and points of right until one of left and right is empty.
            if left[i][0] < right[j][0]:
                h1 = left[i][1]
                self.appendToResult(result, [left[i][0], max(h1, h2)])
                i += 1
            elif left[i][0] > right[j][0]:
                h2 = right[j][1]
                self.appendToResult(result, [right[j][0], max(h1, h2)])
                j += 1
            else:
                h1, h2 = left[i][1], right[j][1]
                self.appendToResult(result, [left[i][0], max(h1, h2)])
                i += 1
                j += 1
        
        while i < len(left):                                                                #If there is still points in left, append the points which are not the same high with the last points of result into result.
            self.appendToResult(result, left[i])
            i += 1
        while j < len(right):
            self.appendToResult(result, right[j])                                           #If there is still points in right, append the points which are not the same high with the last points of result into result.
            j += 1
            
        return result

    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        if not len(buildings):
            return []
        if len(buildings) == 1:                                                             #If there is only one building, return the upper left point and the lower right point.
            return [[buildings[0][0], buildings[0][2]], [buildings[0][1], 0]]
        mid = (len(buildings) + 1) // 2                                                     #Divide the buildings into 2 subsets and recursively calculate the skyline for each subset.
        left, right = self.getSkyline(buildings[:mid]), self.getSkyline(buildings[mid:])
        return self.merge(left, right)     
        
#Heap solution:
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        points = []
        end = {}
        for l, r, h in buildings:                                               #Convert every building to 2 points.
            points.append((l, -h))                                              #The first one is the upperleft point with negative height indicating the beginning of building.
            points.append((r, h))                                               #The second one is the uppreright point with positive height indicationg the end of building.
            end[(l, -h)] = (r, h)                                               #Use a dict to store the map relation of beginning point and end point of same building.
        points.sort()                                                           #Sort points according to x coordinate.
        heap = []                                                               #Use a min heap to store current buildings. The heap top is the beginning point(y coordinate in the first) of current highest building(smallest negative height).
        result = []
        for x, y in points:                                                     #Check every point.
            if y < 0:                                                           #If it's a beginning point and heap is empty or y is smaller than y of the heap top, add current point to result(positive height).
                if not heap or heap[0][0] > y:
                    result.append([x, -y])
                heapq.heappush(heap, (y, x))                                    #Push current point to heap.
            else:
                while heap != [] and end[(heap[0][1], heap[0][0])][0] <= x:     #If it's an ending point, pop every beginning points whose x of corresponding ending point is smaller than current x.
                    heapq.heappop(heap)
                r = []
                if not heap:                                                    #If heap is empty now, potential result point r is current x as x and 0 as y.
                    r = [x, 0]
                elif heap[0][0] > -y:                                           #Otherwise, if the y of heap top is smaller than current y, potential result point r is current x as x and -y of heap top as y.
                    r = [x, -heap[0][0]]
                if r != [] and result[-1] != r:                                 #If r exists and does not equal to last point of result, append r to result.
                    result.append(r)
        return result                                                           #Return result.
