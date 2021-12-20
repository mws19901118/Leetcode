class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()                                        #Sort arr.
        result, minAbs = [], 200001                       #Initialize result and minimum absolute difference.
        for i in range(len(arr) - 1):                     #Traverse arr.
            diff = arr[i + 1] - arr[i]                    #Compute the absolute difference between current pair.
            if diff < minAbs:                             #If diff < minAbs, update minAbs and clear result.
                minAbs = diff
                result.clear()
            if diff == minAbs:                            #If diff == minAbs, append current pair to result.
                result.append([arr[i], arr[i + 1]])
        return result
