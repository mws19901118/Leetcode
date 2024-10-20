class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        def process(operator: str, prev: bool, curr: bool) -> bool:          #Process boolean operation with operator, previous bool and current bool.
            if operator == '!':                                              #Process not.
                return not curr
            elif operator == '&':                                            #Process and.
                return prev and curr
            elif operator == '|':                                            #Process or.
                return prev or curr
            else:                                                            #Process no operator.
                return curr
            
        stack = []                                                           #Use a stack to store all unfinished operators and intermediate results.
        operator, prev = '', None                                            #Initialize operator and previous result.
        for index in range(len(expression)):                                 #Traverse expression.
            if expression[index] == ',' or expression[index] == '(':         #If current character is ',' or '(', continue.
                continue
            if expression[index] == ')':                                     #If current character is ')', pop the last operator and result from stack.
                lastOperator, lastResult = stack.pop()
                prev = process(lastOperator, lastResult, prev)               #Process prev with last result and last operator.
                operator = lastOperator                                      #Set operator to last operator.
            elif expression[index] in ['t', 'f']:                            #If current character is 't' or 'f', parse current bool.
                curr = expression[index] == 't'
                prev = process(operator, prev, curr)                         #Process curr with prev and operator.
            else:                                                            #Otherwise, current character is '|', '&' ir '|'.
                stack.append((operator, prev))                               #Append current operator and result to stack.
                operator = expression[index]                                 #Update operator.
                prev = expression[index] == '&'                              #Update prev.
        return prev                                                          #Return prev.
