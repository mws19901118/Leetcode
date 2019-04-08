import copy
class Solution:
    def backtracking(self, candidates, trace, currentSum, target, result):
        if currentSum == target:
            result.append(copy.deepcopy(trace))                                                             #Deepcopy trace to result.
        elif currentSum < target:
            for i in range(len(candidates)):
                if i != 0 and candidates[i] == candidates[i - 1]:                                           #Eliminate duplication.
                    continue
                trace.append(candidates[i])
                self.backtracking(candidates[i + 1:], trace, currentSum + candidates[i], target, result)    #Because elements in combination should be non-descending and only appear once, use candidates[i + 1:] in the next step.
                trace.pop()
            
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()                                                                                   #Sort the candidates.
        result = []
        self.backtracking(candidates, [], 0, target, result)                                                #Backtracking
        return result
