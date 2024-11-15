class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        j = len(arr) - 1                                        #Find the smallest j such that arr[j:] is non-decreasing.
        while j - 1 >= 0 and arr[j - 1] <= arr[j]:
            j -= 1
        result = j                                              #Then, we can remove arr[:j], so j is the initial result.
        i = 0
        while i < j and (i == 0 or arr[i - 1] <= arr[i]):       #Traverse from the start while arr[:i + 1] is non-decreasing.
            while j < len(arr) and arr[i] > arr[j]:             #While j is not the end and arr[i] > arr[j], move forward j.
                j += 1
            result = min(result, j - i - 1)                     #So now remove arr[i + 1:j] then arr[:i + 1] and arr[j:] is non-decreasing, so update result oif j - i - 1 is smaller.
            i += 1                                              #Move forward i.
        return result
