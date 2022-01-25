class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        i = 0
        while i + 1 < len(arr) and arr[i + 1] > arr[i]:     #Traverse to the first number that are greater than its next if exist.
            i += 1
        if i == 0 or i == len(arr) - 1:                     #If peak is at either end of array, return false.
            return False
        while i + 1 < len(arr) and arr[i + 1] < arr[i]:     #Keep traversing until reaches the end or the next number is greater than current number.
            i += 1
        return i == len(arr) - 1                            #Return whether the traverse reaches the end.
