class Solution:
    def smallestNumber(self, pattern: str) -> str:
        start = 1                                                      #Initialize start at 1.
        i = 0
        while i < len(pattern) and pattern[i] == 'D':                  #If there are x 'D' in the beginning, increase start by x.
            start += 1
            i += 1
        result = [start]                                               #Initialize result with start.
        max_v = start                                                  #Keep track of the max number so far,
        for i, x in enumerate(pattern):                                #Traverse pattern.
            if x == 'D':                                               #If x is 'D', append last number minus 1.
                result.append(result[-1] - 1)
            else:                                                      #Otherwise, find how many consecutive 'D' are behind current 'I'.
                j = 1
                while i + j < len(pattern) and pattern[i + j] == 'D':
                    j += 1
                result.append(max_v + j)                               #Append max_v + j to result, because all the numbers before max_v are used and we have to reserve room for next j 'D'.
                max_v = result[-1]                                     #Update max number.                        
        return "".join(str(x) for x in result)                         #Convert each digit to str and join them and return.
