class Solution:
    def generateString(self, str1: str, str2: str) -> str:
        n, m = len(str1), len(str2)                                    #Get the lengths of str1 and str2.
        s = ["a"] * (n + m - 1)                                        #Initialize the result string characters array to all "a" to make it Lexicographically smallest. 
        fixed = [False] * (n + m - 1)                                  #Also initialize whether the value at each position has to be fixed.
        for i, x in enumerate(str1):                                   #Traverse str1.
            if x == "T":                                               #Handle the case of "T" in str1.
                for j, y in enumerate(str2, i):                        #Traverse str2 and add i to index automatically.
                    if fixed[j] and s[j] != y:                         #If s[j] already has a fixed value and does not equal to y, return empty string.
                        return ""
                    s[j], fixed[j] = y, True                           #Set s[j] to y and mark it as fixed.

        for i, x in enumerate(str1):                                   #Traverse str1 again.
            if x == "F":                                               #Handle the case of "F" in str1.
                if any(y != s[j] for j, y in enumerate(str2, i)):      #If s[i:i + m] is already not equal to str2, skip now.
                    continue
                for j in reversed(range(i, i + m)):                    #Traverse i + m to i backwards.
                    if not fixed[j]:                                   #If current position is not fixed, update it to "b" and stop.
                        s[j] = "b"
                        break
                else:                                                  #If cannot find such position, return empty string.
                    return ""
                  
        return "".join(s)                                              #Join s and return.
