class Solution:
    def search(self, low: int, high: int, num: int, result: List[int]) -> None:     #Search sequential digit.
        if num > high:                                                              #If digit is greater than high bound, return.
            return
        if num >= low:                                                              #If digit is greater than or equal to low bound, add it to result.
            result.append(num)
        lastDigit = num % 10
        if lastDigit < 9:                                                           #If last digit is smaller than 9, calculate next sequential digit.
            num = num * 10 + lastDigit + 1
            self.search(low, high, num, result)
            
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        result = []
        for i in range(1, 9):                                                       #Search for sequential digit starting from 1 to 8.
            self.search(low, high, i, result)
        return sorted(result)                                                       #Sort result.
