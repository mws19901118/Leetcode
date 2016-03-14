#Divide and conquer solution:
class Solution:
    def merge(self,left,right):
        i=0
        j=0
        result=[]
        h1=0                                                                      #Represent the current height from the left skyline.
        h2=0                                                                      #Represent the Current height from the right skyline.
        while i<len(left) and j<len(right):                                       #Compare points of left and points of right until one of left and right is empty.
            if left[i][0]<right[j][0]:
                h1=left[i][1]
                new=[left[i][0],max(h1,h2)]
                if result==[] or result[-1][1]!=new[1]:
                    result.append(new)
                i+=1
            elif left[i][0]>right[j][0]:
                h2=right[j][1]
                new=[right[j][0],max(h1,h2)]
                if result==[] or result[-1][1]!=new[1]:
                    result.append(new)
                j+=1
            else:
                h1=left[i][1]
                h2=right[j][1]
                new=[left[i][0],max(h1,h2)]
                if result==[] or result[-1][1]!=new[1]:
                    result.append(new)
                i+=1
                j+=1
        
        while i<len(left):                                                      #If there is still points in left, append the points which are not the same high with the last points of result into result.
            if result==[] or result[-1][1]!=left[i][1]:
                result.append(left[i])
            i+=1
        while j<len(right):
            if result==[] or result[-1][1]!=right[j][1]:                        #If there is still points in right, append the points which are not the same high with the last points of result into result.
                result.append(right[j])
            j+=1
            
        return result
        
    # @param {integer[][]} buildings
    # @return {integer[][]}
    def getSkyline(self, buildings):
        l=len(buildings)
        if l==0:
            return []
        if l==1:                                                                #If there is only one building, return the upper left point and the lower right point.
            return [[buildings[0][0], buildings[0][2]], [buildings[0][1], 0]]
        mid=(l+1)/2                                                             #Divide the buildings into 2 subsets and recursively calculate the skyline for each subset.
        left=self.getSkyline(buildings[:mid])
        right=self.getSkyline(buildings[mid:])
        return self.merge(left, right)                                          #Merge the result of 2 subsets.
        
#Heap solution:
import heapq
class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        points = []
        dict = {}
        for b in buildings:                                                     #Convert every building to 2 points.
            points.append((b[0], -b[2]))                                        #The first one is the upperleft point with negative height indicating the beginning of building.
            points.append((b[1], b[2]))                                         #The second one is the uppreright point with positive height indicationg the end of building.
            dict[(b[0], -b[2])] = (b[1], b[2])                                  #Use a dict to store the map relation of beginning point and end point of same building.
        points.sort()                                                           #Sort points according to x coordinate.
        hq = []                                                                 #Use a min heap to store current buildings. The heap top is the beginning point(y coordinate in the first) of current highest building(smallest negative height).
        result = []
        for p in points:                                                        #Check every point.
            if p[1] < 0:                                                        #If it's a beginning point and heap is empty or its y is smaller than y of the heap top, add current point to result(positive height).
                if hq == [] or hq[0][0] > p[1]:
                    result.append([p[0], -p[1]])
                heapq.heappush(hq, (p[1], p[0]))                                #Push current point to heap.
            else:
                while hq != [] and dict[(hq[0][1], hq[0][0])][0] <= p[0]:       #If it's an ending point, pop every beginning points whose x of corresponding ending point is smaller than current x.
                    heapq.heappop(hq)
                r = []
                if hq == []:                                                    #If heap is empty now, potential result point r is current x as x and 0 as y.
                    r = [p[0], 0]
                elif hq[0][0] > -p[1]:                                          #Otherwise, if the y of heap top is smaller than current y, potential result point r is current x as x and -y of heap top as y.
                    r = [p[0], -hq[0][0]]
                if r != [] and result[-1] != r:                                 #If r exists and does not equal to last point of result, append r to result.
                    result.append(r)
        return result                                                           #Return result.
