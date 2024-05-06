class Solution(object):
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def checkValid(s: str) -> bool:                       #Check if a string is valid.
            count = 0
            for c in s:
                if c not in '()':
                    continue
                elif c == '(':
                    count += 1
                elif c == ')' and not count:
                    return False
                else:
                    count -= 1
            return not count

        
        if checkValid(s):                                    #If the original string is valid, return q.
            return [s]
        q = set([s])                                         #Store unvalid strings in current level.
        result = []
        while not result:                                    #BFS until there is valid result.
            newq = set()                                     #Initialize the new queue.
            for x in q:                                      #Check every string in q.
                for i in range(len(x)):                      #Generate new strings by remove a parenthesis from x.
                    news = x[:i] + x[i + 1:]                 
                    if news in newq:                         #If news is in newq, skip.
                        continue
                    newq.add(news)                           #Add news to newq.
                    if checkValid(news):                     #If the new string is valid, append it to result.
                        result.append(news)
            q = newq                                         #Replace q with newq.
