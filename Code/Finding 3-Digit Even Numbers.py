class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        count = Counter(digits)                              #Count the digits.
        result = []
        for x in range(100, 1000, 2):                        #Traverse all 3-digit even numbers without leading zeros.
            c = Counter(str(x))                              #Count each digit.
            if all(c[y] <= count[int(y)] for y in c):        #If all digits in x can be found in count, append x to result.
                result.append(x)
        return result
