class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        characters = []                   #Store valid characters.
        stack = []                        #Use a stack to store indexes of '('.
        for i, x in enumerate(s):         #Traverse s.
            c = x                         #Get current character to append to characters.
            if x == '(':                  #If current characer is '(', push the index to stack.
                stack.append(i)
            elif x == ')':                #If current characer is ')', pop stack if stack is not empty, otherwise this ')' is invalid so set c to ''.
                if stack:
                    stack.pop()
                else:
                    c = ''
            characters.append(c)          #Append c to characters.
        for x in stack:                   #For remaining indexes in stack, their '(' is invalid, so set the corresponding characters to ''.
            characters[x] = ''
        return ''.join(characters)        #Join characters and return.
