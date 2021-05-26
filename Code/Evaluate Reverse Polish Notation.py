class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []                                                      #Store numbers using stack,
        for token in tokens:                                            #Traverse tokens.
            if token not in ["+", "-", "*", "/"]:                       #If token is number, append it to stack.
                stack.append(int(token))
            else:                                                       #Otherwise, pop stack twice to get 2 numbers for operation.
                x = stack.pop()
                y = stack.pop()
                if token == "+":                                        #Handle "+".
                    stack.append(x + y)
                elif token == "-":                                      #Handle "-".
                    stack.append(y - x)
                elif token == "*":                                      #Handle "*".
                    stack.append(x * y)
                else:                                                   #Handle "/".
                    sign = 1 if x * y > 0 else -1 
                    stack.append(abs(y) // abs(x) * sign)
        return stack[0]                                                 #Return the only number in stack.
