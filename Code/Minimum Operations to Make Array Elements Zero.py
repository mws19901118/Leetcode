class Solution:
    def minOperations(self, queries: List[List[int]]) -> int:
        @cache                                                                                    #Cache result.
        def calculate(num: int) -> int:                                                           #Calculate the total operations to move all numbers from 1 to num(inclusive) to 0.
            mask, count = 1, 0                                                                    #Initialize the bit mask and count.
            while mask <= num:                                                                    #Iterate while mask is not greater than num.
                count += ((mask.bit_length() + 1) // 2) * (min(mask * 2 - 1, num) - mask + 1)     #There are min(mask * 2 - 1, num) - mask + 1 numbers at current big length, and each of them needs (mask.bit_length() + 1) // 2 operation.
                mask <<= 1                                                                        #Left shift mask by 1 bit.
            return count
        
        return sum((calculate(r) - calculate(l - 1) + 1) // 2 for l, r in queries)                #For each query l and r, the number of operations is (calculate(r) - calculate(l - 1) + 1) // 2; sum of for each query and return.
