class Solution:
    def countOfAtoms(self, formula: str) -> str:
        count = Counter()                                                                                            #Count each type of atom.
        multipliers, nextIndexAfterParentheses = defaultdict(int), defaultdict(int)                                  #Store the multiplier for each pair of parentheses amd the next index after each pair of parentheses.
        stack = []                                                                                                   #Initialize the stack of left parenthese.
        for i, x in enumerate(formula):                                                                              #Traverse formula.
            if x == '(':                                                                                             #If x is left parenthese, append the i to stack.
                stack.append(i)
            elif x == ')':                                                                                           #If x is right parenthese, find the digits after it.
                j = i + 1
                while j < len(formula) and formula[j].isdigit():
                    j += 1
                multipliers[stack.pop()] = int(formula[i + 1:j]) if i + 1 < j else 1                                 #Pop stack and set its multiplier to be the int value of the digits after right parenthese(or 1 if none).
                nextIndexAfterParentheses[i] = j                                                                     #Set the next index after parenthese of i to j.
        stack = [1]                                                                                                  #Use a stack to store the effective multipler for current atom.
        i = 0
        while i < len(formula):                                                                                      #Traverse formula.
            if formula[i] == '(':                                                                                    #If formula[i] is left parenthese, multiply its multiplier to current multiplier and append the result to stack, then move i to i +1.
                stack.append(stack[-1] * multipliers[i])
                i += 1
            elif formula[i] == ')':                                                                                  #If formula[i] is right parenthese, pop stack and move i to nextIndexAfterParentheses[i].
                stack.pop()
                i = nextIndexAfterParentheses[i]
            elif formula[i].isupper():                                                                               #If formula[i] is upper case, find the name first, depending on if there is a lower case after it.
                name = formula[i:i + 2] if i + 1 < len(formula) and formula[i + 1].islower() else formula[i]
                j = i + len(name)
                while j < len(formula) and formula[j].isdigit():                                                     #Find all digits after the name.
                    j += 1
                currCount = 1 if j == i + len(name) else int(formula[i + len(name):j])                               #Its count is the int value of the digits or 1 if none.
                count[name] += currCount * stack[-1]                                                                 #Multiply the count with current multipler and add it to count[name[.
                i = j                                                                                                #Move i after digits.
        result = []
        for x in sorted(count.keys()):                                                                               #Traverse the sorted keys of counter.
            result.append(x)                                                                                         #Append name to result.
            result.append(str(count[x]) if count[x] > 1 else "")                                                     #Append its count(or empty string) to result.
        return "".join(result)                                                                                       #Join and return.
