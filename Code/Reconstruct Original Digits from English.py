class Solution:
    def originalDigits(self, s: str) -> str:
        count = Counter(s)                        #Count letters in s.
        digits = [0] * 10                         #Store the count of each digit.
        
        digits[0] = count['z']                    #Only 'one' has 'z', so the count of 'one' equals to count of 'z'.
        for x in "zero":
            count[x] -= digits[0]                 #Remove all letters from 'one'.
        
        digits[2] = count['w']                    #Only 'two' has 'w', so the count of 'two' equals to count of 'w'.
        for x in "two":
            count[x] -= digits[2]                 #Remove all letters from 'two'.
            
        digits[4] = count['u']                    #Only 'four' has 'u', so the count of 'four' equals to count of 'u'.
        for x in "four":
            count[x] -= digits[4]                 #Remove all letters from 'four'.
            
        digits[5] = count['f']                    #After all letters from 'four' are removed, only 'five' has 'f', so the count of 'five' equals to count of 'f'.
        for x in "five":
            count[x] -= digits[5]                 #Remove all letters from 'five'.
            
        digits[6] = count['x']                    #Only 'six' has 'x', so the count of 'six' equals to count of 'x'.
        for x in "six":
            count[x] -= digits[6]                 #Remove all letters from 'six'.
        
        digits[7] = count['v']                    #After all letters from 'five' are removed, only 'seven' has 'v', so the count of 'seven' equals to count of 'v'.
        for x in "seven":
            count[x] -= digits[7]                 #Remove all letters from 'seven'.
        
        digits[8] = count['g']                    #Only 'eight' has 'g', so the count of 'eight' equals to count of 'g'.
        for x in "eight":
            count[x] -= digits[8]                 #Remove all letters from 'eight'.
        
        digits[9] = count['i']                    #After all letters from 'five' and 'six' are removed, only 'nine' has 'i', so the count of 'nine' equals to count of 'i'.
        for x in "nine":
            count[x] -= digits[9]                 #Remove all letters from 'nine'.
            
        digits[1] = count['o']                    #After all letters from 'zero', 'two' and 'four' are removed, only 'one' has 'o', so the count of 'one' equals to count of 'o'.
        for x in "one":
            count[x] -= digits[1]                 #Remove all letters from 'nine'.
            
        digits[3] = count['h']                    #After all letters from 'eight' are removed, only 'three' has 'h', so the count of 'three' equals to count of 'h'.
        for x in "three":
            count[x] -= digits[3]                 #Remove all letters from 'three'.
            
        result = ""                               #Initialize result to be empty string.
        for i in range(10):                       #Append the count of each digit to result in the order of 0 to 9.
            result += str(i) * digits[i]
        return result
