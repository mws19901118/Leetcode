class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        i, count = 1, 0                    #Initialize i and count.
        bannedSet = set(banned)            #Store banned number in a set.
        while i <= n and i <= maxSum:      #Traverse until i reaches n or maxSum.
            if i not in bannedSet:         #If i is not banned, select i, so substract i from maxSum and increase count.
                maxSum -= i
                count += 1
            i += 1                         #Increase i.
        return count                       #Return count.
