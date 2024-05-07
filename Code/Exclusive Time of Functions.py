class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        stack, result = [], [0] * n                                                            #Initialize stack and result.
        for log in logs:                                                                       #Traverse logs.
            logSplit = log.split(":")                                                          #Split current log.
            id, operation, timestamp = int(logSplit[0]), logSplit[1], int(logSplit[2])         #Extract id, operation and timestamp.
            if operation == "start":                                                           #Process if it is start of a function.
                if stack:                                                                      #If stack is not empty, update the executed time of top of the stack.
                    stack[-1][2] += timestamp - stack[-1][1]
                stack.append([id, timestamp, 0])                                               #Append current id, start time and executed time to stack.
            else:                                                                              #Process if it is end of a function.,
                result[id] += timestamp - stack[-1][1] + 1 + stack[-1][2]                      #Add current executed time and already executed time to result[id].
                stack.pop()                                                                    #Pop stack.
                if stack:                                                                      #If stack is not empty, update the current start time to be the start of next timestamp.
                    stack[-1][1] = timestamp + 1
        return result
