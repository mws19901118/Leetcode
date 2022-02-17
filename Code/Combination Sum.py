class Solution:
    def backtracking(self, candidates: List[int], stack: List[int], currentSum: int, target: int, result: List[List[int]]):
        if currentSum == target:                                                        #If current sum equals target, add a deep copy of stack to result.                
            result.append(copy.deepcopy(stack))
        for i, x in enumerate(candidates):                                              #Traverse candidates.
            if currentSum + x > target:                                                 #If current sum plus current number will exceed target, break.
                break
            stack.append(x)                                                             #Append current number to stack.
            self.backtracking(candidates[i:], stack, currentSum + x, target, result)    #Keep backtracting.
            stack.pop()                                                                 #Pop stack.
            
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()                                                               #Sort the candidates.
        result = []                                                                     #Record the possible combination.
        self.backtracking(candidates, [], 0, target, result)                            #Backtracking.
        return result
