class Solution:
    # @param {string} s
    # @return {boolean}
    def isValid(self, s):
        dict={'(':')','[':']','{':'}'}                        #Store the valid matches.
        left=['(','[','{']                                    #Store the left bracket.
        stack=[]
        for i in s:
            if stack==[]:                                     #If stack is empty, append i into stack.
                stack.append(i)
            elif stack[-1] in left and i==dict[stack[-1]]:    #If the last element in stack is left bracket and i is right bracket, there is a valid match, then pop stack.
                stack.pop()
            else:                                             #Otherwise, append i into stack.
                stack.append(i)
        return stack==[]                                      #If stack is empty, the string is valid.
