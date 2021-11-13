class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []                                              #Initialize a stack to store temperature and date that has no warmer temperature yet.
        answer = [0] * len(temperatures)                        #Initialize answer.
        for i, x in enumerate(temperatures):                    #Traverse temperatures.
            while stack and stack[-1][0] < x:                   #While stack is not empty and the temperature at top of stack is smaller than current temperature, set answer[stack[-1][1]] to i - stack[-1][1] and pop stack.
                answer[stack[-1][1]] = i - stack[-1][1]
                stack.pop()
            stack.append((x, i))                                #Append current temperature and date to stack.
        return answer                                           #Return answer.
