class Solution:
    def minimumSteps(self, s: str) -> int:
        index, result = 0, 0            #Initialize correct index for next '0' and result. 
        for i, x in enumerate(s):       #Traverse s.
            if x == '0':                #If x is '0', shift it from current index to correct index will take i - index swaps.
                result += i - index
                index += 1              #Also increase index.
        return result
