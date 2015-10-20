class Solution:
    # @param num, a list of integer
    # @return an integer
    def findPeakElement(self, num):
        length=len(num)
        if length==0:
            return None
        elif length==1:
            return 0
        elif length==2:
            if num[0]>num[1]:
                return 0
            else:
                return 1
        else:
            if num[0]>num[1]:                                               //Check the endpoint.
                return 0
            elif num[length-1]>num[length-2]:
                return length-1
            else:
                start=0
                end=length-1
                while start<=end:                                           //Binary search.
                    mid=start+(end-start)/2
                    if num[mid]>num[mid-1] and num[mid]>num[mid+1]:         //If mid is peak point, return its index.
                        return mid
                    elif num[mid]<num[mid-1]:                               //If mid is not peak point and num[mid]<mun[mid-1], there must be at least 1 peak point in the left side of mid, because num[i] ≠ num[i+1].
                        end=mid-1
                    else:                                                   //The other side is similar.
                        start=mid+1
