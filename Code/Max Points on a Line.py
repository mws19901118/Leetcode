# Definition for a point
# class Point:
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution:
    # @param points, a list of Points
    # @return an integer
    def maxPoints(self, points):
        length=len(points)
        if length<2:
            return length
        else:
            result=0
            for i in xrange(length):    #loop for every point
                line={'inf':0}          #dictionary for line, the key is slope,value is count
                repeat=1
                for j in xrange(length):
                    if i==j:
                        continue
                    if points[i].x==points[j].x and points[i].y!=points[j].y:     #vertical situation
                        line['inf']+=1
                    elif points[i].x!=points[j].x:
                        slope=float(points[i].y-points[j].y)/(points[i].x-points[j].x)
                        if not line.has_key(slope):       #current slope is not in the dictionary
                            line[slope]=1
                        else:                             #current slope is in the dictionary
                            line[slope]+=1
                    else:
                        repeat+=1                         #count repeat points
                result=max(result,max(line.values())+repeat)    #update the max points
            return result
