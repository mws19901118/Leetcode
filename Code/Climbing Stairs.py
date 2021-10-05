class Solution:
    def climbStairs(self, n: int) -> int:
        steps = [1, 1]                              #Initialize steps.
        for i in range(2, n + 1):                   #Traverse from 2 to n.
            steps.append(steps[-1] + steps[-2])     #Append the steps for i to be the sum of previous 2 steps.
        return steps[n]                             #Return steps[n].
