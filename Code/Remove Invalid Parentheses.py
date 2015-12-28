class Solution(object):
    def checkValid(self, s):                            #Check if a string is valid.
        stack = []
        for c in s:
            if c == '(':
                stack.append(c)
            elif c == ')':
                if stack == []:
                    return False
                else:
                    stack.pop()
        return stack == []
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        result = []
        q = [s]                                       #Store unvalid strings in current level.
        if self.checkValid(s) is True:                #If the original string is valid, return q.
            return q
        while result == []:                           #BFS until there is valid result.
            dict = {}                                 #Use a dict to rule out duplicates.
            for x in q:                               #Check every string in q.
                for i in range(len(x)):
                    news = x[:i] + x[i + 1:]          #Generate new strings by remove a parenthesis from x.
                    if news in dict:
                        continue
                    else:
                        dict[news] = True
                    if self.checkValid(news) is True: #If the new string is valid, append it to result.
                        result.append(news)
            q = dict.keys()                           #The strings in next level is in the keys of dict.
        return result
