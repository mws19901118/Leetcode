import string
class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        dict = {}                                                           #Count occurrence of each letter.  
        for c in s:
            if c not in dict:
                dict[c] = 1
            else:
                dict[c] += 1
        result = set()                                                      #Store the set of letters without duplicates.
        stack = []                                                          #Use a stack to store letters occurred from beginning to end.
        for c in s:                                                         #Check every letter.
            dict[c] -= 1                                                    #Decrease the count by 1.
            if c in result:                                                 #If current letter is already in the set, ignore it.
                continue
            while stack != [] and stack[-1] > c and dict[stack[-1]] > 0:    #If current letter is smaller than the top of stack(stack is not empty) and there is stack top letter behind current letter, pop stack and remove it from result set.
                result.remove(stack.pop())
            result.add(c)                                                   #Add current letter to result.
            stack.append(c)                                                 #Push current letter to stack.
        return ''.join(stack)                                               #Join the stack and return.
