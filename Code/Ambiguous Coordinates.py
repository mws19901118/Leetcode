class Solution:
    def ambiguousCoordinates(self, s: str) -> List[str]:
        s = s[1:-1]                                                                                                       #Remove bracket for s.
        secondNumber = defaultdict(list)                                                                                  #Cache all possible second numbers for each suffix of s.
        secondNumber[s[-1]].append(s[-1])                                                                                 #The last character is itself no matter if it's '0'.
        i = len(s) - 1                                                                                                    #Check if s has trailing '0'.
        while i >= 1 and s[i] == '0':
            i -= 1
        hasTrailing0 = i < len(s) - 1
        for i in range(min(i, len(s) - 2), 0, -1):                                                                        #Traverse backwards.
            if s[i] == '0' and not hasTrailing0:                                                                          #If current character is '0' and there is no trailing '0', the only valid number is placing dot after current character.
                secondNumber[s[i:]].append("0."+ s[i + 1:])
            elif s[i] != '0':                                                                                             #If current character is not '0', the whole suffix till now is valud.
                secondNumber[s[i:]].append(s[i:])
                if not hasTrailing0:                                                                                      #Also, if there is no trailing '0', insert dot between each pair of adjacent characters.
                    for j in range(i + 1, len(s)):
                        secondNumber[s[i:]].append(s[i:j] + "." + s[j:])
        
        result = []                                                                                                       #Initialize result.
        i = 0                                                                                                             #Check if s has leading 0.
        while i < len(s) and s[i] == '0':
            i += 1
        hasLeading0 = i > 0
        for x in secondNumber[s[1:]]:                                                                                     #Handle the first character no matter if it's '0'.
            result.append("(" + s[0] + ", " + x + ")")

        for i in range(1, len(s) - 1):                                                                                    #Traverse from the second character.
            firstNumber = []                                                                                              #Initialize the possible first number.
            if hasLeading0 and s[i] != '0':                                                                               #If s has leading '0' and current character is not '0', the only valid number is placing dot after first character.
                firstNumber.append("0." + s[1:i + 1])
            elif not hasLeading0:                                                                                         #If s does not have leading '0', the whole prefix till now is valud.
                firstNumber.append(s[:i + 1])
                if s[i] != '0':                                                                                           #Also, if current character is not '0', insert dot between each pair of adjacent characters. 
                    for j in range(i):
                        firstNumber.append(s[:j + 1] + "." + s[j + 1:i + 1])
                        
            for x in firstNumber:                                                                                         #Composite coordinates from first number and second nunber.
                for y in secondNumber[s[i + 1:]]:
                    result.append("(" + x + ", " + y + ")")
        return result
