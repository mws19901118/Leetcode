class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        all_odd, all_even, last_odd, last_even = 0, 0, 0, 0         #Initialize the length of subsequence of all odd, all even, alternate odd and even with last number is odd, alternate odd and even with last number is even.
        for x in nums:                                              #Traverse nums.
            if x & 1:                                               #If x is odd, increase all_odd and update last_odd to last_even + 1.
                all_odd += 1
                last_odd = last_even + 1
            else:                                                   #Otherwise, increase all_even and update last_even to last_odd + 1.
                all_even += 1
                last_even = last_odd + 1
        return max(all_odd, all_even, last_odd, last_even)          #Return the max of them.
