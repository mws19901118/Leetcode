class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        count = Counter(arr)                  #Count each integer in arr.
        for x in sorted(arr, key = abs):      #Sort arr by abs value of each integer and then traverse.
            if not count[x]:                  #If x is all used, continue.
                continue
            if not count[2 * x]:              #If 2 * x is all used, no pair valid for x, return false.
                return False
            count[x] -= 1                     #Decrease x from count.
            count[2 * x] -= 1                 #Decrease 2 * x from count.
        return True                           #Return true at the end.
