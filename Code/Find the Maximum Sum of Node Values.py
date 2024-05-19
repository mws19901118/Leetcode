class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
                                                                                                #For each node non adjacent ndoe u, v, if we want to apply opeartions on both, we have to apply all edges connecting u and v.
                                                                                                #But for all intermediate nodes on the path,operations will be applied on them twice, so their values do not change(x ^ k ^ k = x).
                                                                                                #Then u, v is effectively adjacent.
                                                                                                #Also, since operations apply on both nodes, the total number of applied operation node has to be even.
        result, count = 0, 0                                                                    #Initialize result and count of nodes applied operation.
        positiveMin, negativeMax = inf, -inf                                                    #Initialize the min positive delta and max negative delta.
        for x in nums:                                                                          #Traverse nums.
            delta = x ^ k - x                                                                   #Calculate the delta for current node when applied operation.
            result += x                                                                         #Add x to result.
            if delta > 0:                                                                       #If delta is greater than 0, applying operation on current node will benefit the result.
                positiveMin = min(positiveMin, delta)                                           #Update positive min if necessary.
                result += delta                                                                 #Also add delta to result.
                count += 1                                                                      #Increase count.
            else:
                negativeMax = max(negativeMax, delta)                                           #Otherwise, update negative max if necessary.
        return result if not count & 1 else max(result - positiveMin, result + negativeMax)     #If count is even, just return result; otherwise, return the max result of either ecludes positive min or includes negative max, because the total number of applied operation node has to be even.
