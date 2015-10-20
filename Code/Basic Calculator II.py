class Solution:
    # @param {string} s
    # @return {integer}
    def calculate(self, s):
        s = re.sub(r'\d+', ' \g<0> ', s)                                                        #Use regular expression to add space between operators and numbers.
        p = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.floordiv}   #Use dictionary to store each operation and corresponding character.
        expression = s.split()                                                                  #Split the string to operators and numbers.
        result=0
        number=0                                                                                #Record current number to be operated.
        i=0
        func = op['+']                                                                          #Record the operator to be processed. To add the first number, the first operator should always be '+'.
        while i < len(expression):
            e = expression[i]
            if e in '+-':                                                                       #Because there is no parentheses, we can directly calculate the result before the '+' or '-' operators.
                result = func(result, number)
                func = op[e]                                                                    #Set func to current operator.
            elif e in '*/':                                                                     #If current operator is '*' or '/', calculate the answer immediately and update number.
                i += 1
                number = op[e](number, int(expression[i]))
            else:                                                                               #If e is a number, convert from string to int to get it.
                number = int(e)
            i += 1
        return func(result, number)                                                             #Process the last operator and return result.
