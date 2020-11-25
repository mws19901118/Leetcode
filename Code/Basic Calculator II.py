class Solution:
    def calculate(self, s: str) -> int:
        numberStack = []                                                    #Use stack to store number.
        i, lastOperator = 0, '+'                                            #Initial position for traverse and inital operator.
        while i < len(s):
            j = i + 1
            while j < len(s) and s[j] not in {'+', '-', '*', '/'}:          #Find next operator.
                j += 1
            x = int(s[i:j].strip())                                         #Convert the string from current position to next operator to int(after strip) x.
            if lastOperator == '*':                                         #If last operator is '*', pop the stack and multiply x by the number.
                x = numberStack.pop() * x
            elif lastOperator == '/':                                       #If last operator is '/', pop the stack and divide it by x(need to handle if it's negative) then replace x with result.
                y = numberStack.pop()
                x = abs(y) // x * (1 if y >= 0 else -1)
            elif lastOperator == '-':                                       #If last operator is '-', replace x with -x.
                x = -x
            numberStack.append(x)                                           #Append x to stack.
            i = j + 1                                                       #Move i to j + 1.
            if j < len(s):                                                  #Update last operator if j is not out of bound.
                lastOperator = s[j]
        return sum(numberStack)                                             #Return sum of stack.
