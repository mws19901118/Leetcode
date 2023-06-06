class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()                                                                            #Sort arr.
        return all(arr[i] - arr[i - 1] == arr[1] - arr[0] for i in range(1, len(arr)))        #Return all the differences between adjacent elements are same.
