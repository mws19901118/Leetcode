class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        count, i = 0, 0                                                           #Initialize count and pointer.
        while i < len(colors):                                                    #Traverse colors.
            j = i + 1
            while j < len(colors) and colors[i] == colors[j]:                     #Find all consecutive same colors.
                j += 1
            count += sum(neededTime[i:j]) - max(neededTime[i:j])                  #add the sum of needed time minus the max needed time for each consecutive same color.
            i = j
        return count                                                              #Return count.
