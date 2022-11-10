class Solution:
    def maximum69Number (self, num: int) -> int:
        s = list(str(num))          #Covert num to string and split.
        for i in range(len(s)):     #Traverse s.
            if s[i] == '6':         #Convert first '6' to '9'.
                s[i] = '9'
                break
        return int("".join(s))      #Join s, convert to int and return.
