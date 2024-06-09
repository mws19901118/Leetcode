class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        s = [0]                                                         #Store remainder of prefix sum from nums[0] to nums[i]. Add 0 to represent that in the beginning, the sum is 0.
        for x in nums:                                                  #Append the newest remainder to s.
            s.append((s[-1] + x) % k)                                   #Count the occurence of each remainder.
        return sum(v * (v - 1) // 2 for v in Counter(s).values())       #For each pair of indexes, i and j, if s[i] = s[j], then s[i] + (nums[i] + ... + nums[j]) % k = s[j].
                                                                        #Thus, nums[i] to nums[j] is a subarray whose sum is divisible by k.
                                                                        #Then, we only need to calculate for each remainder, how many pairs are there.
                                                                        #If remainder s occurs v times, the number of pairs is v * (v - 1) // 2.
