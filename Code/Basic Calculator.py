class Solution:
    def calculate(self, s: str) -> int:
        stack = [0]                                                             #Initialize a stack to store number and operator.
        sign, currentNumber = '+', 0                                            #Initialize current sign and number.
        operation = {'+': lambda x, y: x + y, '-': lambda x, y: x - y}          #Use lambda function to represent plus and minus.
        s = '(' + s + ')'                                                       #Add parentheses outside s.
        for x in s:                                                             #Traverse s.
            if x == ' ':                                                        #If x is space, skip it.
                continue
            elif x.isdigit():                                                   #If x is dight, update current number.
                currentNumber = currentNumber * 10 + int(x)
            elif x == '+' or x == '-':                                          #If x is '+' or '-', calculate the result with stack[-1] and update stack[-1].
                stack[-1] = operation[sign](stack[-1], currentNumber)
                sign, currentNumber = x, 0                                      #Set sign to x and clear current number.
            elif x == '(':                                                      #If x is '(', append current sign to stack and append 0 as starting a new calculation inside parentheses.
                stack.append(sign)
                stack.append(0)
                sign, currentNumber = '+', 0                                    #Set sign to '+' and clear current number.
            elif x == ')':                                                      #If x is ')', calculate the result with stack[-1] and update stack[-1].
                stack[-1] = operation[sign](stack[-1], currentNumber)
                currentNumber = stack.pop()                                     #Pop the result inside parentheses.
                perviousSign = stack.pop()                                      #Pop the operator before parentheses.
                stack[-1] = operation[perviousSign](stack[-1], currentNumber)   #Merge the result inside parenteses with previous result.
                sign, currentNumber = '+', 0                                    #Set sign to '+' and clear current number.
        return stack[0]                                                         #Return stack[0].
