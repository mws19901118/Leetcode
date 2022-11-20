class Solution:
    def calculate(self, s: str) -> int:
        stack = [(0, '+')]                                                                  #Use a stack to store number and operator, initially number is 0 and operator is '+'.
        currentNumber = 0                                                                   #Initialize current number.
        operation = {'+': lambda x, y: x + y, '-': lambda x, y: x - y}                      #Use lambda function to represent plus and minus.
        s = '(' + s + ')'                                                                   #Add parentheses outside s.
        for x in s:                                                                         #Traverse s.
            if x == ' ':                                                                    #If x is space, skip it.
                continue
            elif x.isdigit():                                                               #If x is dight, update current number.
                currentNumber = currentNumber * 10 + int(x)
            elif x == '+' or x == '-':                                                      #If x is '+' or '-', calculate the result with stack[-1] and update stack[-1].
                stack[-1] = (operation[stack[-1][1]](stack[-1][0], currentNumber), x)
                currentNumber = 0                                                           #Clear current number.
            elif x == '(':                                                                  #If x is '(', append current append (0, '+') to stack to start a new calculation inside parentheses.
                stack.append((0, '+'))
                currentNumber = 0                                                           #Clear current number.
            elif x == ')':                                                                  #If x is ')', calculate the result with stack[-1] and update stack[-1].
                stack[-1] = (operation[stack[-1][1]](stack[-1][0], currentNumber), '+')
                currentNumber, sign = stack.pop()                                           #Pop the result inside parentheses.
                stack[-1] = (operation[stack[-1][1]](stack[-1][0], currentNumber), '+')     #Merge the result inside parenteses with previous result.
                currentNumber = 0                                                           #Clear current number.
        return stack[0][0]                                                                  #Return stack[0][0].
