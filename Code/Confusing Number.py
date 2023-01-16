class Solution:
    def confusingNumber(self, n: int) -> bool:
        confusing = {"0": "0", "1": "1", "6": "9", "8": "8", "9": "6"}                                  #Initialize the confusing number mapping.
        s = str(n)                                                                                      #Convert n to string.
        return all(x in confusing for x in s) and "".join(confusing[x] for x in s)[::-1] != s           #Every digit should be confusing then the reverse of string after rotating cannot be same as original string.
