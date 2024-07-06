class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        @cache                                                            #Cache result.
        def backtrack(index: int, cap: int) -> List[int]:                 #Back track to find all combination sum of cap in candidates[i:].
            if index == len(candidates):                                  #If reaches the end of candidates, return an empty list.
                return []
            result = []
            for i in range(index, len(candidates)):                       #Traverse candidates[i:].
                if candidates[i] < cap:                                   #If candidates[i] < cap, append [candidates[i]] extended by each combination sum of cap - candidates[i] in candidates[i + 1:] to result. 
                    for x in backtrack(i, cap - candidates[i]):
                        result.append([candidates[i]] + x)
                elif candidates[i] == cap:                                #If candidates[i] == cap, append [candidates[i]] tp result.
                    result.append([candidates[i]])
                else:                                                     #Otherwise, break.
                    break
            return result                                                 #Return result.

        candidates.sort()                                                 #Sort candidate.
        return backtrack(0, target)                                       #Return the result of backtrack starting from index 0 and target.
