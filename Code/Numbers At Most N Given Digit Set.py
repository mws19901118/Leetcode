class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        count = [0] * 10                                                                              #Preprocessing, count how many valid digits is not greater than current dight.
        for i in range(1, 10):
            count[i] = count[i - 1] + int(str(i) in digits)
        s = str(n)                                                                                    #Covert n to string.
        result = sum(len(digits) ** i for i in range(1, len(s)))                                      #Calculate all valid number whose length is smaller than n. Basically it's the sum of d ** i for i in [1, k - 1], where k is the length of n and d is the size of digits.
        valid = 1                                                                                     #Use valid to store if the digits from the begnining of n to the digit before current digit are all valid digits.
        for i, x in enumerate(s):                                                                     #Traverse through s.
            result += valid * count[max(0, int(x) - 1)] * len(digits) ** (len(s) - 1 - i)             #If the prefix s[:i] is valid, then all combinations of valid number starts with "s[:i]" + "(x - 1)" (if x >= 1) and has length of k(k is the length of n) is valid and we haven't encounter them. So add count[max(0, int(x) - 1)] * d ** (len(s) - 1 - i) to result, d is the size of digits.
            valid *= count[int(x)] - count[max(0, int(x) - 1)]                                        #Keep checking if s[:i + 1] is valid.
        result += valid                                                                               #Add valid to result.
        return result
