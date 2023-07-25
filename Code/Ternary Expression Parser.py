class Solution:
    def parseTernary(self, expression: str) -> str:
        def compute(index: int) -> (str, int):                                                                          #Recursively compute the value of a valid expression starting at index and return the start of next expression.
            if expression[index] in ['T', 'F'] and index + 1 < len(expression) and expression[index + 1] == '?':        #If current index is 'T' or 'False' and next index is valid and is '?', we are entering a ternary expression.
                former, nextIndex = compute(index + 2)                                                                  #Compute the result of former part and get the start of latter part, skipping ':'.
                latter, nextIndex = compute(nextIndex)                                                                  #Compute the result of latter part and get the start of next expression, skipping ':'.
                result = former if expression[index] == 'T' else latter                                                 #Set result based on current character is 'T' or 'F'.
                return result, nextIndex                                                                                #Return result and nextIndex.
            return expression[index], index + 2                                                                         #If we are not entering a ternary expression, we can dirrectly return current character and index + 2, skipping ':'.
        return compute(0)[0]                                                                                            #Return the first part of computing from the beginning.
