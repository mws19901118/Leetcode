class Solution:
    def backtracking(self, candidates, trace, currentSum, target, result):
        if currentSum == target:                                                        #If current sum equals target, add a deep copy of trace to result.                
            result.append(copy.deepcopy(trace))
        for i, x in enumerate(candidates):                                              #Traverse candidates.
            if currentSum + x > target:                                                 #If current sum plus current number will exceed target, break.
                break
            trace.append(x)                                                             #Append current number to trace.
            self.backtracking(candidates[i:], trace, currentSum + x, target, result)    #Keep backtracting.
            trace.pop()                                                                 #Pop trace.
            
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()                                                               #Sort the candidates.
        result = []                                                                     #Record the possible combination.
        self.backtracking(candidates, [], 0, target, result)                            #Backtracking.
        return result
