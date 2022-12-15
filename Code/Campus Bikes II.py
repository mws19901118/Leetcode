class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        masks = {1 << i: bikes[i] for i in range(len(bikes))}                                                                                                           #Create a mapping between each bit mask to bike.
        @cache                                                                                                                                                          #Cache result.
        def dp(index: int, mask: int):                                                                                                                                  #Iterate with the index of next worker to assign and states of all bikes in a bit mask.
            if index == len(workers):                                                                                                                                   #If reaches the end of workers, return 0.
                return 0
            return min(abs(workers[index][0] - masks[x][0]) + abs(workers[index][1] - masks[x][1]) + backtrack(index + 1, x | mask) for x in masks if not x & mask)     #Traverse each bike in masks, if x & mask is 0, current bike is not assigned, assign it to current worker and iterate to next worker. Return the min distance from now on.

        return dp(0, 0)                                                                                                                                                 #Return dp(0, 0).
