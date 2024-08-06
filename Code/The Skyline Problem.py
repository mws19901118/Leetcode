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
        points, heap, removed = [], [], Counter()                               #Initialize points, max heap and a counter for heights to be removed from heap.
        for l, r, h in buildings:                                               #Convert every building to 2 points.
            points.append((l, -h))                                              #The first one is the upperleft point with negative height indicating the beginning of building.
            points.append((r, h))                                               #The second one is the uppreright point with positive height indicationg the end of building.
        points.sort()                                                           #Sort points according to x coordinate.
        result = []
        for x, y in points:                                                     #Check every point.
            if y < 0:                                                           #If it's a beginning point and heap is empty or y is smaller than y of the heap top, add current point to result(positive height).
                if not heap or heap[0] > y:
                    result.append([x, -y])
                heapq.heappush(heap, y)                                         #Push current height to heap.
            else:
                removed[-y] += 1                                                #If it's an ending point, increase -h in removed.
                while heap and removed[heap[0]]:                                #While the top of heap should be removed, pop it from heap and update removed.
                    removed[heapq.heappop(heap)] -= 1
                height = -heap[0] if heap else 0                                #If heap is empty now, current height for result point is 0; otherwise, it is -y of heap top as y.
                if not result or result[-1][1] != height:                       #If result is empty or current height does not equal to the height of last point of result, append [x, height] to result.
                    result.append([x, height])
        return result                                                           #Return result.
