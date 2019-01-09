class Solution(object):
    def powerfulIntegers(self, x, y, bound):
        """
        :type x: int
        :type y: int
        :type bound: int
        :rtype: List[int]
        """
        expx = [1]                            #Find all the power of x which is smaller than bound.
        p = x
        while p < bound and p > expx[-1]:     #Current power has to be larger than the last one to avoid dead loop when x is 1.
            expx.append(p)
            p *= x
        expy = [1]                            #Find all the power of y which is smaller than bound.
        p = y
        while p < bound and p > expy[-1]:     #Current power has to be larger than the last one to avoid dead loop when y is 1.
            expy.append(p)
            p *= y
        powerful = set()                      #Use a set to store all possible powerful integers.
        for i in expx:
            for j in expy:
                if i + j <= bound:
                    powerful.add(i + j)       #Traverse each pair of power of x and power y, if the sum of them is not larger than bound, add to the set.
                else:
                    break
        return list(powerful)                 #Return the set as list.
