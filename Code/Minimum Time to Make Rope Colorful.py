class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        count, i = 0, 0                                                           #Initialize count and pointer.
        while i < len(colors):                                                    #Traverse colors.
            j = i + 1
            while j < len(colors) and colors[i] == colors[j]:                     #Find all consecutive same colors.
                j += 1
            if j - i > 1:                                                         #If it's more than 1, add the sum of needed time minus the max needed time.
                count += sum(neededTime[i:j]) - max(neededTime[i:j])
            i = j
        return count                                                              #Return count.
