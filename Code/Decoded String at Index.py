class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        stack = []                                                            #Use a stack to store the index and tape length of each character.
        length = 0                                                            #Initially, tape length is 0.
        for i, x in enumerate(s):                                             #Traverse s.
            length = (length * int(x)) if x.isdigit() else (length + 1)       #Update tape length based on if x is digit(multiply by int(x) if x is digit; otherwise increase by 1).
            stack.append((i, length))                                         #Append index and tape length to stack.
            if length >= k:                                                   #If tape length is equal to or greater than k, stop because we don't nede to process further.
                break
        while stack:                                                          #Traverse back while stack is not empty.
            i, x = stack.pop()                                                #Pop stack.
            if s[i].isdigit():                                                #If s[i] is digit, find the equivalant new k in the repeated chunk.
                k = (k - 1) % stack[-1][1] + 1
            elif x == k:                                                      #If length is k, return s[i].
                return s[i]
