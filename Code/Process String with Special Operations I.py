class Solution:
    def processStr(self, s: str) -> str:
        result = []                    #Initialize result.
        for x in s:                    #Traverse s.
            if x == '*':               #If x == '*', pop result if it is not empty.
                if result:
                    result.pop()
            elif x == '#':             #If x == '#', double result.
                result *= 2
            elif x == '%':             #If x == '%', reverse result.
                result.reverse()
            else:                      #Otherwise, append x to result.
                result.append(x)
        return "".join(result)         #Join result and return.
