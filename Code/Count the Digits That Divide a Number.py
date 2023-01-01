class Solution:
    def countDigits(self, num: int) -> int:
        return sum(num % int(x) == 0 for x in str(num))     #Traverse digits; if digit can divide number, increase count.
