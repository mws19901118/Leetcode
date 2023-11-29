class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        length = defaultdict(int)                              #Store the length of max consecutive 1s by index.
        i = 0
        while i < len(nums):                                   #Traverse nums.
            if not nums[i]:                                    #If nums[i] is 0, increase length[i] by 1 to flip it and move to next.
                length[i] += 1
                i += 1
                continue
            j = i + 1                                          #If nums[i] is 1, find the end of current consecutive 1s.
            while j < len(nums) and nums[j]:
                j += 1
            length[i - 1] += j - i                             #Increase length[i - 1] by the length of consecutive 1s, because if flip nums[i - 1], it will become consecutive as well.
            length[j] += j - i                                 #Increase length[j] by the length of consecutive 1s, because if flip nums[j], it will become consecutive as well.
            i = j                                              #Move i to j.
        return max(length.values())                            #Return the max of values of length.
