class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()                                                                                   #Sort the candidates.
        result = []
        def backtracking(stack: List[int], index: int, remain: int) -> None:
            if not remain:                                                                                  #If reaches target. deepcopy stack to result.
                result.append(stack.copy())
                return
            for i in range(index, len(candidates)):                                                         #Traverse candidates[index:].
                if candidates[i] > remain:                                                                  #If candidates[i] > remain, the combination sum will exceeds target, so stop loop here.
                    break
                if i > index and candidates[i] == candidates[i - 1]:                                        #Skip duplicate numbers because we don't need to add all duplicate numbers in one iteration. Let them be handled by later iterations. Otherwise. there will be duplications.
                    continue
                stack.append(candidates[i])                                                                 #Append candidates[i] to stack.
                backtracking(stack, i + 1, remain - candidates[i])                                          #Keep backtracking.
                stack.pop()                                                                                 #Pop stack.

        backtracking([], 0, target)                                                                         #Start backtracking
        return result
