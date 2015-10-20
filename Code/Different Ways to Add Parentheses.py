class Solution:
    # @param {string} input
    # @return {integer[]}
    def diffWaysToCompute(self, input):
        result=[a+b if c == '+' else a-b if c == '-' else a*b     #Divede and conquer at each operator.
            for i, c in enumerate(input) if c in '+-*'            #Use 'enumerate' to get every the index and character.
            for a in self.diffWaysToCompute(input[:i])            #Get the result of expression before c.
            for b in self.diffWaysToCompute(input[i+1:])]         #Get the result of expression after c.
        if result==[]:                                            #If result is none, the expression only has a integer, return it in list.
            return [int(input)]
        else:
            return result
