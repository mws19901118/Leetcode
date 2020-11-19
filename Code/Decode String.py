class Solution:
    def decodeString(self, s: str) -> str:
        numStack, strStack = [], [""]                                           #Initialize 2 stacks, one for number, the other one for string.
        numbers = set(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])       #Use a set to determine if current character is number.
        i = 0
        while i < len(s):                                                       #Traverse through s.
            if s[i] in numbers:                                                 #If current character is number, find where the consecutive numbers end.
                j = i + 1
                while j < len(s) and s[j] in numbers:
                    j += 1
                numStack.append(int(s[i:j]))                                    #Convert the consecutive numbers to int and append it to the number stack.
                i = j + 1                                                       #Because numbers are always followed by a '[', we ignore it and enter an encoded section.
                strStack.append("")                                             #So, append an empty string to string stack as the prefix.
            elif s[i] == ']':                                                   #If current character is ']', generate decoded string in current section.
                decode = strStack.pop() * numStack.pop()                        #Pop number stack and string stack simultaneously and repeat the string for the number times.
                strStack.append(strStack.pop() + decode)                        #Pop string stack to get prefix, append decoded string after prefix and then append it back to string stack.
                i += 1                                                          #Move to next character.
            else:                                                               #If current character is letter, keep updating the last string in string stack.
                strStack.append(strStack.pop() + s[i])
                i += 1
        return strStack[-1]                                                     #Return the last string in string stack.
