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
        
