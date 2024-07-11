class Solution:
    def reverseParentheses(self, s: str) -> str:
        pairs = {}                                 #Store matching pair of parentheses in a dictionary.
        stack = []                                 #Store the index of unmatches left parenthese in the order of visiting them.
        for i, x in enumerate(s):                  #Traverse s.
            if x == '(':                           #If x is left parenthese, append i to stack.
                stack.append(i)
            elif x == ')':                         #If x is right parenthese, match it with top of stack. So, point the index to each other in pairs.
                pairs[i] = stack[-1]
                pairs[stack.pop()] = i
        result = []
        index, delta = 0, 1                        #Use a pointer to traverse s and initially the delta is 1.
        while len(result) < len(s) - len(pairs):   #Iterate while len(result) is smaller than result length, which is the length of s deduct by the length of pairs.
            if s[index].isalpha():                 #If s[index] is character, append it to result and move index.
                result.append(s[index])
                index += delta
            else:                                  #Otherwise, move to the opposite matching parenthese then move back 1 delta because we have to reverse the substring inside.
                index = pairs[index] - delta
                delta = -delta                     #Now, index move in the opposite direction.
        return "".join(result)                     #Join result and return.
