class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        result, start = inf, 0                                              #Initialize result and start of sliding window.
        bit_counts = [0] * 32                                               #Count each bit in or result.
        masks = [1 << i for i in range(32)]                                 #Store the masks for each bit.

        def update_bit_counts(number: int, delta: int) -> None:             #Update bit count for given number with delta(increase 1 or decrease 1),
            for i in range(32):                                             #Traverse bit 0 to 31.
                if number & masks[i]:                                       #If given number contains current bit, update corresponding count with delta.
                    bit_counts[i] += delta

        def check_or_at_least_k() -> int:                                   #Check if OR result is at least k.
            or_result = 0                                                   #Convert bit count back to OR result.
            for i in range(32):
                if bit_counts[i]:
                    or_result |= masks[i]
            return or_result >= k                                           #Return if or result is at least k.
            
        for i in range(len(nums)):                                          #Traverse nums to enumerate the end of sliding window.
            update_bit_counts(nums[i], 1)                                   #Add nums[i] to OR result.
            while start <= i and check_or_at_least_k():                     #While start is not greater than i and OR result is still at least k, move forward start.
                result = min(result, i - start + 1)                         #Update result if current sliding window size is smaller than result. 
                update_bit_counts(nums[start], -1)                          #Move nums[start] out of OR result.
                start += 1

        return -1 if result == inf else result                              #Return -1 if result is inf; otherwise return result.
