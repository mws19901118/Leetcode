class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        result = []
        for length in range(len(str(low)), len(str(high)) + 1):    #Enumerate the possible length from low to high.
            for i in range(1, 11 - length):                        #Enumerate the possible starting digit for each length.
                num = i
                for j in range(i + 1, i + length):                 #Generate number based on the length and starting digit.
                    num = num * 10 + j
                if low <= num <= high:                             #If it is within the range, append it to result.
                    result.append(num)
        return result
