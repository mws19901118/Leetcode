class Solution:
    def romanToInt(self, s: str) -> int:
        romanNegative = {"IV": -1, "XL": -10, "CD": -100, "IX": -1, "XC": -10, "CM": -100}      #Map Roman 4, 40, 400 and 9, 90, 900 to its negative value, -1, -10 or -100.
        romanPositive = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}       #Map other Roman to its value.
        result = 0
        for i in range(len(s)):                                                                 #Scan s.
            if i + 1 < len(s) and s[i:i + 2] in romanNegative:                                  #If s[i:i + 2] is 4, 40, 400 or 9, 90, 900, add the negative value to result.
                result += romanNegative[s[i:i + 2]]
            else:                                                                               #Otherwise, add its value to result.
                result += romanPositive[s[i]]
        return result                                                                           #Return result.
