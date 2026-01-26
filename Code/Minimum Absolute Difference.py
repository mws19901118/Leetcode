class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()                                                                                            #Sort arr.
        minDifference = min(arr[i + 1] - arr[i] for i in range(len(arr) - 1))                                 #Calculate the min difference.
        return [[arr[i], arr[i + 1]] for i in range(len(arr) - 1) if arr[i + 1] - arr[i] == minDifference]    #Return all pairs with min difference.
