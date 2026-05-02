class Solution:
    def rotatedDigits(self, n: int) -> int:
        rotation = {"0": "0", "1": "1", "2": "5", "3": "-", "4": "-", "5": "2", "6": "9", "7": "-", "8": "8", "9": "6"}    #Store the rotation for each digit; "-" means invalid.
        count = 0
        for x in range(1, n + 1):                                                                                          #Traverse from 1 to n inclusively.
            s = str(x)                                                                                                     #Convert x to string.
            y = "".join([rotation[d] for d in s])                                                                          #Get the rotated string.
            if "-" not in y and y != s:                                                                                    #The rotated string must be valid and not equal to s; if so, increase count.
                count += 1
        return count
                    
