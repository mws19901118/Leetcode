class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        result = 1                                                                  #Each single element is a turbulent subarray, so result is at least 1.
        i = 0
        while i < len(arr) - 1:
            if arr[i] == arr[i + 1]:                                                #If arr[i] == arr[i + 1], arr[i] cannot be the start of turbulent subarray longer than 1, so move to next element.
                i += 1
            else:
                sign = (arr[i + 1] > arr[i]) - (arr[i + 1] < arr[i])                #Get the sign of arr[i + 1] - arr[i].
                j = i
                while j < len(arr) - 1 and (arr[j + 1] - arr[j]) * sign > 0:        #Check it's in the same turbulent subarray until the subarray ends. To be in the same turbulent subarray, (arr[j + 1] - arr[j]) * sign > 0.
                    j += 1
                    sign = -sign                                                    #Flip the sign.
                result = max(result, j - i + 1)                                     #Update result.
                i = j                                                               #Move i to the end of current turbulent subarray to search for the next turbulent subarray.
        return result
