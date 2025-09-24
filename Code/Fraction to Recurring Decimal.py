class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        flag = "-" if numerator / denominator < 0 else ""                                               #If the result is negative, add a minus flag.
        numerator, denominator = abs(numerator), abs(denominator)                                       #Take the absolute value of numerator and denominator.
        quotient, remain = divmod(numerator, denominator)                                               #Calculate the initial integer quotient and remain.
        if not remain:                                                                                  #If no remain, just return the integer quotient as string with flag.
            return flag + str(quotient)
        stack = []                                                                                      #Store decimal digits in a list.
        visited = defaultdict(int)                                                                      #Store the corresponding digits index in stack for each remain.
        while remain and remain not in visited:                                                         #Iterate while remain is not 0 and not visited.
            digit, newRemain = divmod(remain * 10, denominator)                                         #Calculate the current digit for quotient and new remain after divide remain * 10 by denominator.
            visited[remain] = len(stack)                                                                #Set the index in visited for remain.
            stack.append(str(digit))                                                                    #Append digit as string to stack.
            remain = newRemain                                                                          #Update remain with new remain.
        decimal = ""                                                                                    #Initailize decimal string.
        if not remain:                                                                                  #If no remain, just join the stack.
            decimal = "".join(stack)
        else:                                                                                           #Otherwise, join the stack before the index of remain, add left parentheses, join the rest of stack and add right parentheses.
            decimal = "".join(stack[:visited[remain]]) + "(" + "".join(stack[visited[remain]:]) + ")"
        return flag + str(quotient) + "." + decimal                                                     #Return the concatenation of flag, quotient as string, dot and decimal.
