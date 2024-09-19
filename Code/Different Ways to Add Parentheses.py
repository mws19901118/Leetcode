class Solution:
    @cache
    def diffWaysToCompute(self, expression: str) -> List[int]:
        result = [a + b if c == '+' else a - b if c == '-' else a * b     #Divede and conquer at each operator.
            for i, c in enumerate(expression) if c in '+-*'               #Use 'enumerate' to get every the index and character.
            for a in self.diffWaysToCompute(expression[:i])               #Get the result of expression before c.
            for b in self.diffWaysToCompute(expression[i + 1:])]          #Get the result of expression after c.
        return [int(expression)] if not result else result                #If result is empty, expression is just a number so return it in a list; otherwise, return result.
