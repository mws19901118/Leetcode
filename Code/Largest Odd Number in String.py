class Solution:
    def largestOddNumber(self, num: str) -> str:
        oddDigits = set(["1", "3", "5", "7", "9"])        #Odd digits set.
        for i in reversed(range(len(num))):               #Traverse num backwards.
            if num[i] in oddDigits:                       #If current digit is odd, return the substring from beginning to current digit.
                return num[:i + 1]
        return ""                                         #Otherwise there is no odd number, so return empty string.
