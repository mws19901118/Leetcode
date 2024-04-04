class Solution:
    def maxDepth(self, s: str) -> int:
        count, result = 0, 0                        #Count the current depth.
        for x in s:                                 #Traverse s.
            if x == "(":                            #If x is left parenthes, increase count and update result if necessary.
                count += 1
                result = max(result, count)
            elif x == ")":                          #If x is right parenthes. derease count.
                count -= 1
        return result
