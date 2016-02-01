class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        if preorder == '':                                      #If preoder is empty, return true.
            return True
        p = preorder.split(',')                                 #Split preorder by ','.
        if p[0] == '#':                                         #If the root is '#', it's valid only if the length of p is 1. 
            return len(p) == 1
        stack = [(p[0], 0)]                                     #Append the root to stack.
        i = 1                                                   #Record the current node.
        while stack != [] and i < len(p):                       #While stack is not empty and current node is valid, do the followings:
            if p[i] != '#':                                     #If current node is not '#', append a tuple to stack.
                stack.append((p[i], 0))                         #The first value of the tuple is value of current node, the second value is an int. 0 indicates we havn't finished traversing its left child.
                i += 1                                          #Go to next node.
            else:                                               #Otherwise, if stack is not empty, pop the stack.
                if stack != []:
                    node = stack.pop()
                    if node[1] == 0:                            #If the second value of the popped tuple is 0, set it to 1 and append the modified tuple to stack.
                        stack.append((node[0], 1))              #1 indicates we have finished traversing the left child but haven't finished traversing the right child.
                        i += 1
        return stack == [] and i == len(p) - 1                  #If stack is empty and we exactly traversed every node, the preorder is valid; otherwise, it's invalid.
