class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        used, result = set(), [0] * (2 * n - 1)                                                  #Initialize a set to store used number and initialize result list with 2 * n - 1 length.
        def backtracking(index: int) -> bool:                                                    #Backtracking to fill number at current index, assuming every index before current index are already filled.
            if index == 2 * n - 1:                                                               #If index reaches the end, return true.
                return True
            for i in reversed(range(1, n + 1)):                                                  #Traverse from n to 1.
                if i in used or (i > 1 and (index + i >= (2 * n - 1) or result[index + i])):     #If i is used or i is greater than 1 and either index + i is invalid or result[index + i] is already set, skip i.
                    continue
                used.add(i)                                                                      #Add i to used.
                result[index] = i                                                                #Set result[index] to i.
                if i > 1:                                                                        #If i > 1, also set result[index + i] to i.
                    result[index + i] = i
                j = index + 1                                                                    #Find the next unfilled index.
                while j < 2 * n - 1 and result[j]:
                    j += 1
                if backtracking(j):                                                              #Keep backtracking at j; if we found a solutiom, return true as well.
                    return True
                used.remove(i)                                                                   #Restore used, result[index] and result[index + i] if i > 1.
                result[index] = 0
                if i > 1:
                    result[index + i] = 0
        
        backtracking(0)                                                                           #Start backtracking at index 0.
        return result
