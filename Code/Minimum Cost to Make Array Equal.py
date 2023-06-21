class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        numsWithCost = sorted([(x, y) for x, y in zip(nums, cost)])                                                                    #Sort numbers and its cost by numbers increasingly.
        prefixSumForCost, suffixSumForCost = [0], [0]                                                                                  #Initialize the prefix sum and suffix sum for current order of numbers.
        runningCost = 0                                                                                                                #Initialize running cost.
        for i in range(len(numsWithCost)):                                                                                             #Traverse numsWithCost.
            prefixSumForCost.append(prefixSumForCost[-1] + numsWithCost[i][1])                                                         #Calculate prefix sum and append to prefixSumForCost.
            suffixSumForCost.append(suffixSumForCost[-1] + numsWithCost[-(i + 1)][1])                                                  #Calculate suffix sum and append to suffixSumForCost.
            runningCost += (numsWithCost[i][0] - numsWithCost[0][0]) * numsWithCost[i][1]                                              #Updating runningCost to set all numbers equal to numsWithCost[0][0].
        minCost = runningCost                                                                                                          #Initialize minCost to be runningCost.
        for i in range(1, len(numsWithCost)):                                                                                          #Traverse all the gaps between nums. Because min cost can only be achieved if all numbers equal to any existing number. See proof below. 
            runningCost += (numsWithCost[i][0] - numsWithCost[i - 1][0]) * (prefixSumForCost[i] - suffixSumForCost[-(i + 1)])          #Update running cost, for all numbers before i, increase gap while for all numbers after i decrease gap; in total it is gap * (prefixSumForCost[i] - suffixSumForCost[-(i + 1)]).
            minCost = min(minCost, runningCost)                                                                                        #Update minCost if necessary.
        return minCost                                                                                                                 #Proof, suppose we have 2 numbers x, y with cost A and B respectively. 
                                                                                                                                       #The cost to equalize at x F(x) = abs(x - y) * B.
                                                                                                                                       #The cost to equalize at y F(y) = abs(x - y) * A.
                                                                                                                                       #The cost to equalize at z in (x, y) F(z) = abs(x - z) * A + abs(y - z) * B.
                                                                                                                                       #If A < B, then F(z) > abs(x - z) * A + abs(y - z) * A = F(y); similarly, if A > B then F(z) > F(x).
                                                                                                                                       #If A == B, then F(z) = F(x) = F(y). Thus F(z) >= min(F(x), F(y)).
                                                                                                                                       #So, generalizing for n numbers, min cost can only be achieved if all numbers equal to any existing number.
