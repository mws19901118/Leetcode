class Solution:
    def minimumCosts(self, regular: List[int], express: List[int], expressCost: int) -> List[int]:
        currentRegular, currentExpress = 0, expressCost                                        #Store current stop min cost for regular and express; initially at stop 0, they are 0 and expressCost respectively.
        result = []                                                                            #Initialze result.
        for r, e in zip(regular, express):                                                     #Traverse regular and express together.
            currentRegular = min(currentRegular + r, currentExpress + e)                       #New min cost for regular is the smaller of traveling from last regular and traveling from last express.
            currentExpress = min(currentRegular + expressCost, currentExpress + e)             #New min cost for express is the smaller of traveling from current regular and traveling from last express.
            result.append(min(currentRegular, currentExpress))                                 #Append the smaller of currentRegular and currentExpress to result.
        return result
