class Solution:
    def brokenCalc(self, X: 'int', Y: 'int') -> 'int':
        result = 0                        #Work backward, using "divide by 2" and "add 1" to reach X from Y. Take "divide by 2" as many as possible.
        while X < Y:                      #While Y is larger than X, add 1 if it is odd, else divide by 2. 
            while X < Y and Y % 2 == 0:
                Y /= 2
                result += 1
            if X < Y:
                Y += 1
                result += 1

        result += int(X - Y)              #Then, we need to do X - Y additions to reach X
        return result
