class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        i, j = 0, 0                                   #Start traverse from 0 and the start of arr.
        while k:
            i += 1                                    #Increase i.
            if j < len(arr) and i == arr[j]:          #If i == arr[j], i is not missing, so move to next element in arr.
                j += 1
            else:                                     #Otherwise i is missing, decrease k.
                k -= 1
        return i                                      #Return i when k == 0.
