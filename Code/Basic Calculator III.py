class Solution:
    def calculate(self, s: str) -> int:
        def operation(operator: str, number: int, stack: List[int]) -> None:      #Calculate result.
            if operator == '+':                                                   #If opeartor is '+', append number to stack.
                stack.append(number)
            elif operator == '-':                                                 #If opeartor is '-', append -number to stack.
                stack.append(-number)
            elif operator == '*':                                                 #If opeartor is '*', pop previous number and calculate the product then append to stack.
                stack.append(stack.pop() * number)
            elif operator == '/':                                                 #If opeartor is '/', pop previous number and calculate the quotient then append to stack.
                stack.append(int(stack.pop() / number))
        
        
        def dfs(index: int) -> (int, int):                                        #DFS from s[index], returning the result and ending index.
            stack = []                                                            #Initialize stack to store numbers.
            number, operator = 0, '+'                                             #Initialize current number to be 0 and current operator to be '+'.
            while index < len(s):                                                 #Traverse s from index.
                if s[index].isdigit():                                            #If s[index] is digit, update number.
                    number = number * 10 + int(s[index])
                elif s[index] in '+-*/':                                          #If s[index] is operator, calculate the result and reset number and operator.   
                    operation(operator, number, stack)
                    number, operator = 0, s[index]
                elif s[index] == '(':                                             #If s[index] is '(', start dfs from index + 1.
                    (number, index) = dfs(index + 1)                              #Update number and index to be the result of dfs.
                elif s[index] == ')':                                             #If s[index] is ')', finish the last operation.
                    operation(operator, number, stack)
                    return sum(stack), index                                      #Return the sum of stack and index.
                index += 1                                                        #Move index forward.

            operation(operator, number, stack)                                    #Finish the last operation
            return sum(stack), index                                              #Return the sum of stack and index.

        return dfs(0)[0]
