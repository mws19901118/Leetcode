class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack, answer = [], [0] * len(temperatures)             #Initialize a stack to store index of temperature that has no warmer temperature yet and initialize answer.
        for i, x in enumerate(temperatures):                    #Traverse temperatures.
            while stack and temperatures[stack[-1]] < x:        #While stack is not empty and the temperature at the index on top of stack is smaller than current temperature, pop stack.
                index = stack.pop()
                answer[index] = i - index                       #Set answer[index] to i - index.
            stack.append(i)                                     #Append current index to stack.
        return answer                                           #Return answer.
