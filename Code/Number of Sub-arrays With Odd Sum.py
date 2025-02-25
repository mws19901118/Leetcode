class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        prefix_sum_last_bit = 0                                                #Initialize the last bit of prefix sum.
        count = {0: 1, 1: 0}                                                   #Count prefix sum with last bit, initially it is 1 for 0 and 0 for 1.
        result, division = 0, 10 ** 9 + 7                                      #Initialize result and division.
        for x in arr:                                                          #Traverse arr.
            prefix_sum_last_bit ^= x % 2                                       #Update last bit.
            result = (result + count[1 - prefix_sum_last_bit]) % division      #Increase count[1 - prefix_sum_last_bit] to result and take the modulo.
            count[prefix_sum_last_bit] += 1                                    #Update count[prefix_sum_last_bit].
        return result
