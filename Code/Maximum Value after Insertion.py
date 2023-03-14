class Solution:
    def maxValue(self, n: str, x: int) -> str:
        x = str(x)                                              #Convert x to str.
        if n[0] == '-':                                         #If n is negative, find the first digit that is greater than x, then insert before it.
            index = 1
            while index < len(n) and n[index] <= x:
                index += 1
            return n[:index] + x + n[index:]
        else:                                                   #Otherwise, find the first digit that is smaller than x, then insert before it.
            index = 0
            while index < len(n) and n[index] >= x:
                index += 1
            return n[:index] + x + n[index:]
