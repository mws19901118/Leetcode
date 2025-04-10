class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        def calculate(x: str) -> int:                                        #Calculate the powerful int from 1 to int(x).
            if len(x) < len(s):                                              #If x is shorted than s, return 0.
                return 0
            if len(x) == len(s):                                             #If x is same length with s, return if x is greater than s.
                return x >= s
            count, len_diff = 0, len(x) - len(s)                             #Initialize count and compute length diff between x and s.
            for i in range(len_diff):                                        #Traverse len_diff to calculate the power int when fixing the digits in x[:i].
                if limit < int(x[i]):                                        #If limit is smaller than current digit, then any number containing current digit cannot be powerful.
                    count += (limit + 1) ** (len_diff - i)                   #So, we have limit + 1 choices for each digit in x[i:len_diff].
                    return count                                             #Return count.
                count += int(x[i]) * (limit + 1) ** (len_diff - 1 - i)       #Otherwise, we have int(x[i]) choice for current digit and (limit + 1) choinces for each digit in x[i + 1:len_diff].
            return count + (x[len_diff:] >= s)                               #Return count + 1 if the suffix of x is greater than s.

        return calculate(str(finish)) - calculate(str(start - 1))            #Return the count of power int from 1 to str(finish) minus the count of int from 1 to str(start - 1).
