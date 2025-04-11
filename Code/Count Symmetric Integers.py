class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count = 0                                                                                                          #Initialize count.
        for i in range(low, high + 1):                                                                                     #Traverse from low to high.
            digits = str(i)                                                                                                #Convert i to string.
            mid = len(digits) // 2                                                                                         #Calculate mid index.
            count += not len(digits) & 1 and sum(int(x) for x in digits[:mid]) == sum(int(x) for x in digits[mid:])        #Increase count if number have even digits and it is symmetric.
        return count
