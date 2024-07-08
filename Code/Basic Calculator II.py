class Solution:
    def calculate(self, s: str) -> int:
        operations = {'+': lambda x, y: x + y, '-': lambda x, y: x - y, '*': lambda x, y: x * y, '/': lambda x, y: int(x / y)}            #Define operations as lambda functions.
        result, prevOperator, prevNumber, currNumber = 0, '+', 0, 0                                                                       #Initialize result, previous operator, previous number and current number.
        s += '+'                                                                                                                          #Add a '+' to the end of s to finalize the calculation.
        for i, x in enumerate(s):                                                                                                         #Traverse s.
            if x == " ":                                                                                                                  #If x is space, continue.
                continue
            if x.isdigit():                                                                                                               #If x is digit, update current number,
                currNumber = currNumber * 10 + int(x)
            else:                                                                                                                         #Otherwise, update previous number based on the operation.
                prevNumber = operations[prevOperator](prevNumber, currNumber)
                if x in ['+', '-']:                                                                                                       #If x is '+' or '-', previous number has no further impact, so add it to result and reset.
                    result += prevNumber
                    prevNumber = 0
                currNumber = 0                                                                                                            #Reset current number and pervious opeartor.
                prevOperator = x
        return result
