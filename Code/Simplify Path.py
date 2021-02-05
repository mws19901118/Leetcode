class Solution:
    def simplifyPath(self, path: str) -> str:
        splits = path.split("/")                            #Split the string.
        stack = []                                          #Use stack to store valid folder or file name.
        for s in splits:                                    #Traverse splits.
            if not s or s == '.':                           #If s is "" or ".", continue.
                continue
            elif s == "..":                                 #Else if s is ".." and stack is not empty, pop stack.
                if stack:
                    stack.pop()
            else:                                           #Otherwise, append s to stack.
                stack.append(s)
        return "/" + "/".join(stack)                        #Join the stack and return.
