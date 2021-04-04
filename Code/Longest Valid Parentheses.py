class Solution:
    def longestValidParentheses(self, s: str) -> int:
        record = [0] * len(s)                                               #Record the length of longest valid parentheses ending at each character.
        left = []                                                           #It's a stack recording every index of '('.
        for i, x in enumerate(s):                                           #Traverse through the string.
            if x == '(':                                                    #If current character is '(', append the index to left.
                left.append(i)
            elif left != []:                                                #If current character is ')' and left is not empty, pop stack, which is the nearest '(' before current ')'(note as leftindex).
                leftindex = left.pop()
                if i - leftindex == record[i - 1] + 1:                      #If the distance between i and leftindex equals the length of longest valid parentheses ending at i - 1 plus 1, the string from leftindex to i is a valid parentheses.
                    record[i] = record[i - 1] + 2
                    if leftindex > 0:                                       #Combine the longest valid parentheses ending at i and the longest valid parentheses ending at leftindex - 1.
                        record[i] += record[leftindex - 1]
        return max(record) if record else 0                                 #Return the max of record or 0 if record is empty.
